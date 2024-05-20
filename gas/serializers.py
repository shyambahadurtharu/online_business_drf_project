from rest_framework import serializers
from .models import Gas

class GasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gas
        fields = '__all__'

