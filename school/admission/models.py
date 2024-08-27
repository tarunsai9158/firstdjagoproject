from django.db import models


# Create your models here.
class Admission(models.Model):
    stu_name=models.CharField(max_length=100)
    stu_father=models.CharField(max_length=100)
    joindate=models.DateField()
    stu_class=models.CharField(max_length=20,unique=True)
    fee=models.PositiveIntegerField()



    
    
    class Meta:
        verbose_name="Admission"
        verbose_name_plural="Admissions"


