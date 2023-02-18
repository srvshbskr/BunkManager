from django.shortcuts import render,redirect
from .forms import CreateUserForm,createRecordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from .models import Record

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
    r = Record.objects.filter(user =request.user)
    p =0
    a = 0
    t = 0
    for i in r :
        t += 8
        if i.hour1:
            p +=1
        else:
            a+=1
        if i.hour2:
            p +=1
        else:
            a+=1
        if i.hour3:
            p +=1
        else:
            a+=1
        if i.hour4:
            p +=1
        else:
            a+=1
        if i.hour5:
            p +=1
        else:
            a+=1
        if i.hour6:
            p +=1
        else:
            a+=1
        if i.hour7:
            p +=1
        else:
            a+=1
        if i.hour8:
            p +=1
        else:
            a+=1

        per = p/t *100

    context = {'list':r,'t':t,'a':a,'p':p}
    return render(request,'report.html',context)

def createrecordpage(request):

    form = createRecordForm()


    if request.method == 'POST':
        form = createRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createrecord')
        else:
            messages.info(request,'invalid Details')
    context = {'form':form}

    return render(request,'createrecordpage.html',context)

