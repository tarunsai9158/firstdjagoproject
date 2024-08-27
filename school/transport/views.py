from django.shortcuts import render
from django.http import HttpResponse


def transports(request):
    return render(request,'transport.html',{})

# Create your views here.
