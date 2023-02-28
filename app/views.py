from django.shortcuts import render, redirect
from .forms import CreateUserForm, createRecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Record
from django.contrib.auth import get_user_model
from .filters import ReportFilter

def homepage(request):

    context = {}
    return render(request, 'homepage.html', context)


def signuppage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'signuppage.html', context)


def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('report')

        else:
            messages.info(request, 'invalid credentials')
    context = {}
    return render(request, 'login.html', context)


def logoutpage(request):

    logout(request)
    return redirect('login')


@login_required(login_url='login')
def reportpage(request):
    r = Record.objects.filter(user=request.user)
    p = 0
    a = 0
    t = 0
    for i in r:
        t += 8
        if i.hour1:
            p += 1
        else:
            a += 1
        if i.hour2:
            p += 1
        else:
            a += 1
        if i.hour3:
            p += 1
        else:
            a += 1
        if i.hour4:
            p += 1
        else:
            a += 1
        if i.hour5:
            p += 1
        else:
            a += 1
        if i.hour6:
            p += 1
        else:
            a += 1
        if i.hour7:
            p += 1
        else:
            a += 1
        if i.hour8:
            p += 1
        else:
            a += 1
    if t != 0:
        per = p/t * 100
    else:
        per = 0

    context = {'list': r, 't': t, 'a': a, 'p': p, 'pe': per}
    return render(request, 'report.html', context)


def createrecordpage(request):

    form = createRecordForm()

    if request.method == 'POST':
        form = createRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createrecord')
        else:
            messages.info(request, 'invalid Details')
    context = {'form': form}

    return render(request, 'createrecordpage.html', context)


def listpage(request):

    user = get_user_model()
    l = user.objects.all()

    rl = {}
    pl = {}
    for i in l:
        rl[i] = Record.objects.filter(user=i)
    for x in rl:
        p = 0
        a = 0
        t = 0
        per = 0
        temp = rl[x]
        for i in temp:
            t += 8
            if i.hour1:
                p += 1
            else:
                a += 1
            if i.hour2:
                p += 1
            else:
                a += 1
            if i.hour3:
                p += 1
            else:
                a += 1
            if i.hour4:
                p += 1
            else:
                a += 1
            if i.hour5:
                p += 1
            else:
                a += 1
            if i.hour6:
                p += 1
            else:
                a += 1
            if i.hour7:
                p += 1
            else:
                a += 1
            if i.hour8:
                p += 1
            else:
                a += 1
        if t != 0:
            per = p/t * 100
        else:
            per = 0
        pl[x] = per
    context = {'pt':pl}
    return render(request, 'list.html', context)




def searchpage(request):

    l = Record.objects.all()
    f = ReportFilter(request.GET,queryset=l)
    l = f.qs
    a=0
    p=0
    t = 0
    for i in l:
        t += 8
        if i.hour1:
            p += 1
        else:
            a += 1
        if i.hour2:
            p += 1
        else:
            a += 1
        if i.hour3:
            p += 1
        else:
            a += 1
        if i.hour4:
            p += 1
        else:
            a += 1
        if i.hour5:
            p += 1
        else:
            a += 1
        if i.hour6:
            p += 1
        else:
            a += 1
        if i.hour7:
            p += 1
        else:
            a += 1
        if i.hour8:
            p += 1
        else:
            a += 1
    if t != 0:
        per = p/t * 100
    else:
        per = 0

    
    context = {'f':f,'l':l,'a':a,'p':p,'t':t,'per':per}
    return render(request, 'singlepage.html', context)


