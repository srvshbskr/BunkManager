from django.shortcuts import render,redirect
from .forms import CreateUserForm,createRecordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from .models import *
import datetime

def homepage(request):

    context = {}
    return render(request,'homepage.html',context)

def signuppage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'signuppage.html',context)


def loginpage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user) 
            return redirect('report')
        
        else:
            messages.info(request,'invalid credentials')
    context ={}
    return render(request,'login.html',context)


def logoutpage(request):

    logout(request)
    return redirect('login')    

@login_required(login_url='login')
def reportpage(request):
    reports = Record.objects.filter(user = request.user)
    attended = 0
    absent = 0
    total = len(reports)*8
    for i in reports:
        if i.hour1:
            attended +=1
        else:
            absent +=1
        if i.hour2:
            attended +=1
        else:
            absent +=1
        if i.hour3:
            attended +=1
        else:
            absent +=1
        if i.hour4:
            attended +=1
        else:
            absent +=1
        if i.hour5:
            attended +=1
        else:
            absent +=1
        if i.hour6:
            attended +=1
        else:
            absent +=1
        if i.hour7:
            attended +=1
        else:
            absent +=1
        if i.hour8:
            attended +=1
        else:
            absent +=1
    percentage = attended/total *100
    percentage =str(percentage)
    context = {'list':reports,'t':total,'p':attended,'a':absent,'pe':percentage[0:5]}
    return render(request,'report.html',context)

def createrecordpage(request):

    form = createRecordForm()


    if request.method == 'POST':
        form = createRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'record added')
            return redirect('report')
            
        else:
            messages.info(request,'invalid Details')
    context = {'form':form}

    return render(request,'createrecordpage.html',context)