from django.contrib import admin
from service.models import Device, Service, Vender, ThirdUser
from django.core.paginator import Paginator
# Register your models here.
@admin.register(Device)
class AdminDevice(admin.ModelAdmin):
    list_display=["device_name"]
@admin.register(Vender)
class AdminVender(admin.ModelAdmin):
    list_display=["vender_name"]
@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display=["device_type","device_info","problem","descriptions","service_number","contact","adress","Service_getter","time_style","updated_at","asap","user","status","vender"]
    list_per_page = 10
@admin.register(ThirdUser)
class AdminThirdUser(admin.ModelAdmin):
    list_display=["name","contact","alternativ_number","province","district","municipality","wada","tole","zipcode","landmark"]
    list_per_page = 10

 