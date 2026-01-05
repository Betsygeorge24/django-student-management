from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def registers(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        Email=request.POST.get("Email")

        User.objects.create_user(username=username, email=Email, password=password)
        return redirect('logins')
    return render(request,'registers.html')
def logins(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"invalid username or password")
            return redirect('logins')
    return render(request,'logins.html')


def logout_user(request):
    logout(request)
    return redirect("logins")


@login_required
def home(request):
    return render(request, "home.html")

def home(request):
    return render(request, "home.html")




# Create your views here.
