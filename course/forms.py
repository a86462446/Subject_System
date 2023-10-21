from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    name = forms.CharField(
        label="姓名",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    classs = forms.CharField(
        label="系級",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'name', 'classs')


class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class SearchForm(forms.Form):
    search_code= forms.CharField(
        label= "選課代碼",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required= False
    )
    search_name= forms.CharField(
        label= "科目名稱",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required= False
    )


class SearchForm2(forms.Form):

    CHOICES= (('', '請選擇'), ('星期一', '星期一'), ('星期二', '星期二'), ('星期三', '星期三'), ('星期四', '星期四'), ('星期五', '星期五'))
    search_week= forms.ChoiceField(choices= CHOICES, label="星期", required= True)

    CHOICES = (('', '請選擇'), (1, '1'), (2, '2'),(3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'))
    search_session= forms.ChoiceField(choices= CHOICES, label= "節次", required= False)
