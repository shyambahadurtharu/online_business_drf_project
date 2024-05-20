from rest_framework import serializers
from .models import Service, Device, ThirdUser

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
class ThirdUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdUser
        fields = "__all__"