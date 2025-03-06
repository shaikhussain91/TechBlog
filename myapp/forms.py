from django import forms
from .models import *
from django.contrib.auth.models import User

class techblogForm(forms.ModelForm): 
    class Meta:
        model = techblog
        fields =['title','discription','photo']

class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name','password']

class loginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)