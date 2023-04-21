# from django import forms

# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=100)
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)