from django.db import models
from django.conf import settings
class Status(models.TextChoices):
    ORDERED = ("ordered","Ordered")
    VERIFIED = ("verified","Verified")
    ON_THE_WAY = ("on_the_way","On_the_way")
    DELIVERED = ("delivered","Delivered")
    CANCELL_USER = ("cancell_user","Cancell_user")
    CANCELL_admin = ("cancell_admin","Cancell_admin")
class Device(models.Model):
    device_name = models.CharField(max_length=100)
    def __str__(self):
        return self.device_name
class Vender(models.Model):
    vender_name = models.CharField(max_length=100)
    def __str__(self):
        return self.vender_name
class Service(models.Model):
    device_type = models.ForeignKey(Device, on_delete=models.CASCADE)
    device_info = models.CharField(max_length=255)
    problem = models.TextField()
    descriptions = models.TextField()
    Service_getter=models.TextField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    time_style = models.CharField(max_length=255, default="default" )
    updated_at = models.DateTimeField(auto_now=True)
    asap=models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    status = models.CharField(max_length=100, choices=Status.choices, default= Status.ORDERED)
    service_number = models.CharField(max_length=100, blank=True, null=True)
    vender = models.ForeignKey(Vender, on_delete=models.CASCADE, blank=True, null=True)
    
class ThirdUser(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    name = models.TextField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    alternativ_number=models.CharField(max_length=20, blank=True, null=True)
    province=models.CharField(max_length=200, blank=True, null=True)
    district=models.CharField(max_length=100, blank=True, null=True)
    municipality=models.CharField(max_length=200, blank=True, null=True)
    wada=models.CharField(max_length=10, blank=True, null=True)
    tole=models.CharField(max_length=100, blank=True, null=True)
    zipcode=models.CharField(max_length=10, blank=True, null=True)
    landmark=models.CharField(max_length=250, blank=True, null=True)
