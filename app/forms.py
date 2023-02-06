from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

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

class createRecordForm(ModelForm):
    
    class Meta:
        model = Record
        fields = "__all__"
