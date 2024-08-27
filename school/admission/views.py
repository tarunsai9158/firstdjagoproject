from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'index.html',{})
def services(request):
    return render(request,'services.html',{})

def products(request):
    return render(request,'products.html',{})



def logi(request):
    return render(request,'login.html',{})

