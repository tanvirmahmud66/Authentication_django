from django.contrib import admin
from main.models import RegistrationData

# Register your models here.


class RegistrationDataFormate(admin.ModelAdmin):
    list_display = ('username', 'email', 'gender', 'password')


admin.site.register(RegistrationData, RegistrationDataFormate)
