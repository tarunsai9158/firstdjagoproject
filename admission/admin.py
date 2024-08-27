from django.contrib import admin
from .models import Admission

class AdmissionAdmin(admin.ModelAdmin):
  list_display=('id','stu_name','stu_father','joindate','stu_class','fee')

admin.site.register(Admission,AdmissionAdmin)


