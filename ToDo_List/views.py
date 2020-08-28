from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import  login_required
from .models import TodoEntry

# Create your views here.

def login_func(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(request,username = request.POST['username'],password = request.POST['password'])
        if user:
            login(request,user)
            return render(request,'index.html')
        else:
            return render(request,'login.html')

def logout_func(request):
    logout(request)
    return redirect('/login')


@login_required()
def newToDo(request):
    if request.method == 'GET':
        return render(request,'newwork.html')
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        t = TodoEntry()
        t.time = request.POST['time']
        t.parentuser = request.user
        t.work = request.POST['work']
    return render(request,'index.html')


