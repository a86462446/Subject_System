from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, SearchForm, SearchForm2
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import course, Student_course, Student
from itertools import chain
from django.contrib.auth.hashers import check_password

# 學生選課主頁
@login_required(login_url="login")
def index(request):
    name_code_form= SearchForm()  # 搜尋課程名稱及課程代碼
    time_form= SearchForm2()    # 搜尋課程時間

    mydata = course.objects.all().values()  # 存取course資料庫所有內容

    if request.method== "POST":

        # 判斷搜尋結果
        if request.POST.get("search_name")or request.POST.get("search_code"):
            search_name= request.POST.get("search_name")    # 取得表單之課程名稱
            search_code= request.POST.get("search_code")    # 取得表單之課程代碼

            if search_name and search_code:
                if course.objects.filter(name= search_name, code= search_code):
                    mydata= course.objects.filter(name= search_name, code= search_code).all()
                else:
                    mydata= ''
            elif search_code:
                if course.objects.filter(code= search_code):
                    mydata= course.objects.filter(code= search_code).all()
                else:
                    mydata= ''
            elif search_name:
                if course.objects.filter(name= search_name):
                    mydata= course.objects.filter(name= search_name).all()
                else:
                    mydata= ''
        elif request.POST.get("search_week")or request.POST.get("search_session"):
            search_week= request.POST.get("search_week")
            search_session= request.POST.get("search_session")

            if search_week and search_session:
                data= ''
                if course.objects.filter(week= search_week):
                    for item in course.objects.filter(week= search_week):
                        st_start= item.start_session
                        st_end= item.end_session
                        y= st_start

                        # 判斷所有課程內容是否有時間符合搜尋結果
                        for i in range(st_end- st_start+ 1):
                            if int(search_session)== y+ i:
                                data= chain(data, course.objects.filter(code= item).all())
                    mydata= data
                else:
                    mydata= ''
            elif search_week:
                mydata= course.objects.filter(week= search_week).all()

    student= Student.objects.all()  # 存取Student資料庫內容
    student_course= Student_course.objects.all().values()  # 存取Student_course資料庫內容

    # 將資訊存進context回傳至index.html
    context = {
        'mycourses': mydata,
        'Student_courses': student_course,
        'form': name_code_form,
        'form2': time_form,
        'student_form': student
    }
    return render(request, 'index.html', context)

# 登入
def log_in(request):
    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get("username") # 取得帳號
        password = request.POST.get("password") # 取得密碼
        user = authenticate(request, username=username, password=password)  # 驗證用戶是否存在

        # 判斷登入資訊
        if user is not None:
            login(request, user)
            return redirect('/')  #重新導向到首頁
        else:
            try:
                if Student.objects.filter(student_number= username):
                    return render(request, 'login.html', {'error_message': '密碼錯誤，請再試一次。', 'form': form})
                else:
                    return render(request, 'login.html', {'error_message': '帳號不存在，請檢查輸入的帳號。', 'form': form})
            except:
                return render(request, 'login.html', {'error_message': '登入時發生錯誤。', 'form': form})

    return render(request, 'login.html', {'form': form})

# 註冊
def register(request):

    # 取得註冊表單資訊
    registerform = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        # 存取表單內容
        student_number= request.POST.get("username")
        student_name= request.POST.get("name")
        student_class= request.POST.get("classs")

        # 將registerform內容儲存至Student資料庫
        student= Student(student_number= student_number, student_name= student_name, student_class= student_class)
        
        # 重要: 儲存
        student.save()

        if form.is_valid():
            form.save()
            redirect('/login')  #重新導向到登入畫面
            
    # 將資訊存進context回傳至register.html
    context = {
        'registerform': registerform
    }
    return render(request, 'register.html', context)


# 登出
def log_out(request):
    logout(request) # Django內建登出功能
    return redirect('/login') #重新導向到登入畫面

# 加選
def add_course(request, id):
    
    # 存取欲加選之課程資訊
    add= course.objects.all()
    add_start= add[id- 1].start_session
    add_end= add[id- 1].end_session
    add_week= add[id- 1].week
    add_credit= add[id- 1].credit

    # 判斷此學生之學分是否已滿
    for i in Student.objects.filter(student_number= request.user.get_username()):
        if i.student_credit+ add_credit> 25:
            return render(request, 'add_course.html', {'context': '已超過25學分，加選失敗！'})

    # 相同課程處理
    if Student_course.objects.filter(student_number= request.user.get_username(), code= add[id- 1].code):
        return render(request, 'add_course.html', {'context': '已有此課程，加選失敗！'})

    # 衝堂處理
    if Student_course.objects.filter(student_number= request.user.get_username(), week= add_week):
        for item in Student_course.objects.filter(student_number= request.user.get_username(), week= add_week):
            st_start= item.start_session
            st_end= item.end_session
            x= add_start
            y= st_start

            # 判斷是否有衝堂
            for i in range(add_end- add_start+ 1):
                for j in range(st_end- st_start+ 1):
                    if x+ i== y+ j:
                        return render(request, 'add_course.html', {'context': '課堂衝突，加選失敗！'})
    
    # 課程存進Student_course資料庫
    student= Student_course(student_number= request.user.username, code= add[id- 1].code, name= add[id- 1].name, classs= add[id- 1].classs, required_elective= add[id- 1].required_elective, credit= add[id- 1].credit, time= add[id- 1].time, start_session= add[id- 1].start_session, end_session= add[id- 1].end_session, week= add[id- 1].week)
    student.save()

    # 將學分加至用戶學生
    for i in Student.objects.filter(student_number= request.user.username):
        i.student_credit= i.student_credit+ add_credit
        i.save()
    
    return render(request, 'add_course.html', {'context': '加選成功！'})

# 退選
def delete_course(request, code, id):

    # 取得Student_course資料庫內容
    delete= Student_course.objects.all()

    # 將用戶學生之學分扣掉退選課程之學分
    for i in delete.filter(student_number= request.user.username, code= code):
        for j in Student.objects.filter(student_number= request.user.username):
            j.student_credit= j.student_credit- i.credit
            j.save()

    # 將課程從Student_course刪掉
    delete.filter(code= code).delete()

    return redirect('/')
