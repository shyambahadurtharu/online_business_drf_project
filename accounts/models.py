# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
   
    def __str__(self):
        return self.username
    
class KycUser(models.Model):    
    profile_picture=models.ImageField(upload_to="profile_picture/", blank=True, null=True)
    first_name=models.CharField(max_length=100, blank=True, null=True)
    middle_name=models.CharField(max_length=100, blank=True, null=True)
    last_name=models.CharField(max_length=100, blank=True, null=True)
    mobile_number=models.CharField(max_length=100, blank=True, null=True)
    alternativ_number=models.CharField(max_length=100, blank=True, null=True)
    gender=models.CharField(max_length=100, blank=True, null=True)
    occupation=models.CharField(max_length=100, blank=True, null=True)
    qualification=models.CharField(max_length=100, blank=True, null=True)
    dob=models.DateField(max_length=100, blank=True, null=True)
    permanent_province=models.CharField(max_length=200, blank=True, null=True)
    permanent_district=models.CharField(max_length=100, blank=True, null=True)
    permanent_municipality=models.CharField(max_length=200, blank=True, null=True)
    permanent_wada=models.CharField(max_length=100, blank=True, null=True)
    permanent_tole=models.CharField(max_length=200, blank=True, null=True)
    permanent_zipcode=models.CharField(max_length=100, blank=True, null=True)
    permanent_landmark=models.CharField(max_length=250, blank=True, null=True)
    current_province=models.CharField(max_length=200, blank=True, null=True)
    current_district=models.CharField(max_length=100, blank=True, null=True)
    current_municipality=models.CharField(max_length=200, blank=True, null=True)
    current_wada=models.CharField(max_length=100, blank=True, null=True)
    current_tole=models.CharField(max_length=200, blank=True, null=True)
    current_zipcode=models.CharField(max_length=100, blank=True, null=True)
    current_landmark=models.CharField(max_length=250, blank=True, null=True)
    id_other=models.CharField(max_length=100, blank=True, null=True)
    Gathered_name=models.CharField(max_length=100, blank=True, null=True)
    Gathered_mobile=models.CharField(max_length=100, blank=True, null=True)
    Gathered_address=models.CharField(max_length=100, blank=True, null=True)
    Gathered_home_coordination=models.CharField(max_length=200, blank=True, null=True)
    Gathered_description=models.TextField( blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    def __int__(self):
        return self.id
    

class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile_number=models.CharField(max_length=20, blank=True, null=True)
    alternativ_number=models.CharField(max_length=20, blank=True, null=True)
    province=models.CharField(max_length=200, blank=True, null=True)
    district=models.CharField(max_length=100, blank=True, null=True)
    municipality=models.CharField(max_length=200, blank=True, null=True)
    wada=models.CharField(max_length=10, blank=True, null=True)
    tole=models.CharField(max_length=100, blank=True, null=True)
    zipcode=models.CharField(max_length=10, blank=True, null=True)
    landmark=models.CharField(max_length=250, blank=True, null=True)
    