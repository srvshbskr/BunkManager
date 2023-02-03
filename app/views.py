from django.shortcuts import render,redirect
from .forms import CreateUserForm

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
