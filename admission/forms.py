from django import forms


# Create your models here.
class AdmissionForm(forms.Form):
    id=forms.IntegerField()
    stu_name=forms.CharField()
    stu_father=forms.CharField()
    joindate=forms.DateField()
    stu_class=forms.CharField()
    fee=forms.IntegerField()