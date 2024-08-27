from django.contrib import admin
from .models import Studentprofile

class StudentprofileAdmin(admin.ModelAdmin):
  list_display=('id','stu_name','fee')

admin.site.register(Studentprofile,StudentprofileAdmin)
