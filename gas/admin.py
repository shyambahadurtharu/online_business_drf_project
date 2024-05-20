from django.contrib import admin
from gas.models import Gas
from django.core.paginator import Paginator
# Register your models here.

@admin.register(Gas)
class AdminService(admin.ModelAdmin):
    list_display=["user","Service_getter","gas_type","quantity","contact","address","landmark","descriptions_address","time_style","updated_at","asap","status","vender"]
    list_per_page = 10

