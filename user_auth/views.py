from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']


        if password ==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username exist')
                return redirect(user_signup)
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                return redirect('user_login')
    else:
        print("this is no post")
    return render(request,"user/signup.html")

def user_login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
           auth.login(request, user)
           return redirect('/')
       else:
           messages.info(request, 'Invalid')
           return redirect('user_login')

    else: 
        return render(request,'user/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('user_login')

