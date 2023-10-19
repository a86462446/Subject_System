from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, SearchForm, SearchForm2
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import course, D1051831_course
from itertools import chain

# 學生選課主頁
@login_required(login_url="login")  # 限制直接存取登入後畫面
def index(request):
    form= SearchForm()
    form2= SearchForm2()

    D1051831_data= D1051831_course.objects.all().values()
    mydata = course.objects.all().values()  # 存取course資料庫內容

    if request.method== "POST":
        # 判斷搜尋結果
        if request.POST.get("search_name")or request.POST.get("search_code"):
            search_name= request.POST.get("search_name")
            search_code= request.POST.get("search_code")

            if search_name and search_code:
                if course.objects.filter(name= search_name, code= search_code):
                    mydata= course.objects.filter(name= search_name, code= search_code).all()
            elif search_code:
                if course.objects.filter(code= search_code):
                    mydata= course.objects.filter(code= search_code).all()
            elif search_name:
                if course.objects.filter(name= search_name):
                    mydata= course.objects.filter(name= search_name).all()
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

                        for i in range(st_end- st_start+ 1):
                            if int(search_session)== y+ i:
                                data= chain(data, course.objects.filter(code= item).all())
                    
                    mydata= data
                                
            elif search_week:
                if course.objects.filter(week= search_week):
                    mydata= course.objects.filter(week= search_week).all()
            
    context = {
        'mycourses': mydata,
        'D1051831_courses': D1051831_data,
        'form': form,
        'form2': form2
    }
    return render(request, 'index.html', context)


# 登入
def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username") # 取得帳號
        password = request.POST.get("password") # 取得密碼
        user = authenticate(request, username=username, password=password)

        # 登入成功
        if user is not None:
            login(request, user)
            return redirect('/')  #重新導向到首頁
    context = {
        'form': form
    }

    return render(request, 'login.html', context)


# 註冊
def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)

        # 儲存帳密資訊
        if form.is_valid():
            form.save()
            redirect('login/')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


# 登出
def log_out(request):
    logout(request)
    return redirect('/login') #重新導向到登入畫面

# 加選
def add_course(request, id):
    add= course.objects.all()

    add_start= add[id- 1].start_session
    add_end= add[id- 1].end_session
    add_week= add[id- 1].week
    x= add_start

    # 相同課程處理
    if D1051831_course.objects.filter(code= add[id- 1].code):
        return render(request, 'add_course.html', {'same_context': '已有此課程，加選失敗！'})

    # 衝堂處理
    if D1051831_course.objects.filter(week= add_week):
        for item in D1051831_course.objects.filter(week= add_week):
            st_start= item.start_session
            st_end= item.end_session
            y= st_start

            for i in range(add_end- add_start+ 1):
                for j in range(st_end- st_start+ 1):
                    if x+ i== y+ j:
                        return render(request, 'add_course.html', {'conflict_context': '課堂衝突，加選失敗！'})
    
    student= D1051831_course(code= add[id- 1].code, name= add[id- 1].name, classs= add[id- 1].classs, required_elective= add[id- 1].required_elective, credit= add[id- 1].credit, time= add[id- 1].time, start_session= add[id- 1].start_session, end_session= add[id- 1].end_session, week= add[id- 1].week)
    student.save()
    return render(request, 'add_course.html', {'success_context': '加選成功！'})

# 退選
def delete_course(request, code, id):
    delete= D1051831_course.objects.all().filter(code= code)
    delete.delete()
    return redirect('/')
