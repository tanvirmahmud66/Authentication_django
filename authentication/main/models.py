from django.db import models

# Create your models here.


class RegistrationData(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    re_password = models.CharField(max_length=100)
