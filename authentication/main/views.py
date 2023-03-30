from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.


def landing(request):
    return render(request, 'landing/landing.html')


def sing_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        password = request.POST["password"]
        repassword = request.POST["retype_password"]
        print(username, email, gender, password, repassword)
    return render(request, 'signup/signup.html')


def log_in(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password)

    return render(request, 'signin/signin.html')


# def home(reqeust):
#     pass
