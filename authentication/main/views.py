from django.shortcuts import render
from main.models import RegistrationData
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
        if password == repassword:
            value = RegistrationData(
                username=username, email=email, gender=gender, password=password)
            value.save()
            return HttpResponseRedirect(reverse('signin'))
        else:
            return HttpResponse(request, "password doesn't match")
    return render(request, 'signup/signup.html')


def log_in(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password)
    return render(request, 'signin/signin.html')


# def home(reqeust):
#     pass
