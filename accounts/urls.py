from django.contrib import admin
from django.urls import path
from accounts.views import *
from admission.views import *



urlpatterns = [
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    


]