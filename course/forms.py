from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    name = forms.CharField(
        label="姓名",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    classs = forms.CharField(
        label="班級",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'classs')


class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    