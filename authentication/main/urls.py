from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.sing_up, name='signup'),
    path('signin/', views.log_in, name='signin'),
]
