from django.db import models


# Create your models here.
class Admission(models.Model):
    # id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=100)
    stu_father=models.CharField(max_length=100)
    joindate=models.DateField()
    stu_class=models.CharField(max_length=100)
    fee=models.PositiveIntegerField()



    
    
    class Meta:
        verbose_name="Admission"
        verbose_name_plural="Admissions"


