from django.shortcuts import render, redirect
from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import course


# 學生選課主頁
@login_required(login_url="login")  # 限制直接存取登入後畫面
def index(request):
    mydata = course.objects.all().values()  # 存取course資料庫內容
    context = {
        'mycourses': mydata,
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

