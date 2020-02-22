from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method == 'POST':
        # THe user wants to sign up!
        if request.POST['InputPassword1'] == request.POST['InputPassword2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'users/signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['InputPassword1'])
                auth.login(request,user)
                return redirect('tasks')
        else:
            return render(request, 'users/signup.html',{'error':'Passwords doesn\'t match'})
    else:
        #The user wants to enter info!
        return render(request, 'users/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['InputPassword1'])
        if user is not None:
            auth.login(request, user)
            return redirect('tasks')
        else:
            return render(request, 'users/login.html',{'error':'Username or password is incorrect'})
    else:
        return render(request, 'users/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'users/logout.html')