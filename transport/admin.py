from django.contrib import admin
from .models import TransportDetail
from .models import RouteDetail

class TransportDetailAdmin(admin.ModelAdmin):
  list_display=('id','stu_name','route','fee')


class RouteDetailAdmin(admin.ModelAdmin):
  list_display=('id','route_name','distance','price')

admin.site.register(TransportDetail,TransportDetailAdmin)
admin.site.register(RouteDetail,RouteDetailAdmin)
