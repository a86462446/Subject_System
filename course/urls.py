from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.sign_up, name='sign_up'),
    path('login', views.sign_in, name= 'login'),
    path('logout', views.log_out, name='Logout')
]