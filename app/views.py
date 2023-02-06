from django.shortcuts import render,redirect
from .forms import CreateUserForm,createRecordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    return render(request,'signuppage.html',context)


def logoutpage(request):

    logout(request)
    return redirect('login')    

@login_required(login_url='login')
def reportpage(request):
    
    context = {}
    return render(request,'report.html',context)