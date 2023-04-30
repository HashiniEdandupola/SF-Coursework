from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid')
            return redirect('user_login')

    else:
        return render(request, 'user/login.html')

def user_signup(request, id=0):
    if request.method == "GET":
        if id==0:
            form = UserForm()
        else:
            user = User.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(request, 'user/signup.html', {'form':form})
    else:
        if id==0:
            form = UserForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('/')


# CRUD
def user_list(request):
    users = User.objects.all()
    # users_count = users.count()
    context = {
        'user_list':users,
    }
    return render(request,'user/user_list.html',context)

def user_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = UserForm()
        else:
            user = User.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(request, 'user/user_form.html', {'form':form})
    else:
        if id==0:
            form = UserForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('/user/list')

def user_delete(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('/user/list')