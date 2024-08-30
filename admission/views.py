from django.shortcuts import render
from django.http import HttpResponse
from admission.models import Admission


def home(request):
    data=Admission.objects.all()
    res=render(request,'index.html',{'studata':data})
    return res
    


def services(request):
    return render(request,'services.html',{})

def products(request):
    return render(request,'products.html',{})



def logi(request):
    return render(request,'login.html',{})

