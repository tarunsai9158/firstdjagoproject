from django.shortcuts import redirect, render
from django.http import HttpResponse
from admission.models import Admission
from admission.forms import AdmissionForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import auth


def home(request):
    data=Admission.objects.all()
    result=data.filter(id=4).exists()

    if result:
        result=data.get(id=4)
    # result=data.get(id=1)
    # data=data.filter(id=1,stu_class='python')

    res=render(request,'index.html',{'data':list(data),'result':result})
    return res

def deleteadmission(request,id):
    result=Admission.objects.get(id=id)
    result.delete()
    return redirect('home')

def editadmission(request,id):
    result=Admission.objects.get(id=id)
    res=render(request,'admissionedit.html',{'result':result})
    return res

def admissionentry(request):
    # admission_form=AdmissionForm()
    if request.method=='POST':
        result=AdmissionForm(request.POST)
        if result.is_valid():
            id=result.cleaned_data['id']
            stu_name=result.cleaned_data['stu_name']
            stu_father=result.cleaned_data['stu_father']
            joindate=result.cleaned_data['joindate']
            stu_class=result.cleaned_data['stu_class']
            fee=result.cleaned_data['fee']
            result=Admission(
                id=int(id),
                stu_name=stu_name,
                stu_father=stu_father,
                joindate=joindate,
                stu_class=stu_class,
                fee=int(fee)
            )
        
            result = Admission(
                    id=int(id),
                    stu_name=stu_name,
                    stu_father=stu_father,
                    joindate=joindate,
                    stu_class=stu_class,
                    fee=int(fee)
                )
            result.save()
                
            return redirect('home')
            
    
    res=render(request,'admissionentry.html',{})
    return res



def services(request):
    return render(request,'services.html',{})

def products(request):
    return render(request,'products.html',{})




    
    # return redirect('/')

