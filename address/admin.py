from django.contrib import admin
from address.models import Province, District, Municipality
# Register your models here.
@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display=["id", "name"]
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display=["id", "name"]
@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display=["id", "name"]
   

