from django.db import models
from django.conf import settings
from service.models import Vender
class Status(models.TextChoices):
    ORDERED = ("ordered","Ordered")
    VERIFIED = ("verified","Verified")
    ON_THE_WAY = ("on_the_way","On_the_way")
    DELIVERED = ("delivered","Delivered")
    CANCELL_USER = ("cancell_user","Cancell_user")
    CANCELL_admin = ("cancell_admin","Cancell_admin")

class Gas(models.Model):
    gas_type = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100, default= 1)
    Service_getter=models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    descriptions_address = models.TextField()
    time_style = models.CharField(max_length=255, default="default")
    updated_at = models.DateTimeField(auto_now=True)
    asap=models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    status = models.CharField(max_length=100, choices=Status.choices, default= Status.ORDERED)
    odered_number = models.CharField(max_length=100, default="2019309300")
    vender = models.ForeignKey(Vender, on_delete=models.CASCADE, blank=True, null=True )
