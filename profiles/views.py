from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import Studentprofile


def profiles(request):
    data=Studentprofile.objects.all()
    res=render(request,'profiles.html',{'stu':data})
    return res

# Create your views here.
