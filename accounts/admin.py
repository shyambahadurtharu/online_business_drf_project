from django.contrib import admin
from accounts.models import CustomUser, Address, KycUser
# Register your models here.
@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display=['username','email','password']
@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display=['user','first_name','middle_name', 'last_name', 'mobile_number', 'alternativ_number', 'province', 'district',
                  'municipality', 'wada', 'tole', 'zipcode', 'landmark']
@admin.register(KycUser)
class AdminKyc(admin.ModelAdmin):
   list_display=['user','profile_picture','first_name','middle_name', 'last_name', 'mobile_number', 'alternativ_number','gender', 'occupation', 'qualification', 'dob', 'permanent_province', 'permanent_district',
                  'permanent_municipality', 'permanent_wada', 'permanent_tole', 'permanent_zipcode', 'permanent_landmark','current_province', 'current_district',
                  'current_municipality', 'current_wada', 'current_tole', 'current_zipcode', 'current_landmark','id_other','Gathered_name','Gathered_mobile','Gathered_address','Gathered_home_coordination','Gathered_description']

    
     