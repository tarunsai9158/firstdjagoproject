from django.db import models

# Create your models here.

class Studentprofile(models.Model):
    stu_name=models.CharField(max_length=100)
    
    fee=models.PositiveIntegerField()




    
    class Meta:
        verbose_name="Studentprofile"
        verbose_name_plural="Studentprofiles"
