from django.shortcuts import render, redirect
# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email == 'admin@gmail.com' and password == 'password':
            return redirect('dashboard')

    else:        
        return render(request, 'admin_login/adminlogin.html')
    
