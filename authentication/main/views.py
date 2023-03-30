from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def landing(request):
    return render(request, 'landing/landing.html')


def sing_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["retype_password"]
        if password == repassword:
            new_user = User.objects.create_user(username, email, password)
            new_user.save()
            return redirect('signin')
    return render(request, 'signup/signup.html')


def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'Home/profile.html')
        else:
            return render(request, 'signin/signin.html')
    return render(request, 'signin/signin.html')
