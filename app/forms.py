from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
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
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs = {'class':'form-field'}
        self.fields['day'].widget.attrs = {'class':'form-field'}
        self.fields['hour1'].widget.attrs = {'class':'form-field'}
        self.fields['hour2'].widget.attrs = {'class':'form-field'}
        self.fields['hour3'].widget.attrs = {'class':'form-field'}
        self.fields['hour4'].widget.attrs = {'class':'form-field'}
        self.fields['hour5'].widget.attrs = {'class':'form-field'}
        self.fields['hour6'].widget.attrs = {'class':'form-field'}
        self.fields['hour7'].widget.attrs = {'class':'form-field'}
        self.fields['hour8'].widget.attrs = {'class':'form-field'}
    class Meta:
        model = Record
        fields = "__all__"
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'})
        }