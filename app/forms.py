from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
     
     def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class':'form-field'}
        self.fields['email'].widget.attrs = {'class':'form-field'}
        self.fields['password1'].widget.attrs = {'class':'form-field'}
        self.fields['password2'].widget.attrs = {'class':'form-field'}

     class Meta:
        model = User
        fields = ['username','email','password1','password2']