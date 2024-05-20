from django.shortcuts import render

# Create your views here.
# views.py

from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Province, District, Municipality
from .serializers import ProvinceSerializer, DistrictSerializer, MunicipalitySerializer
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET'])
def get_province(request):
    if request.method == 'GET':
        province = Province.objects.all()
        serializer = ProvinceSerializer(province, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def get_districts(request, province_id):
    districts = District.objects.filter(province_id=province_id)
    serializer = DistrictSerializer(districts, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_municipalities(request, district_id):
    municipalities = Municipality.objects.filter(district_id=district_id)
    serializer = MunicipalitySerializer(municipalities, many=True)
    return JsonResponse(serializer.data, safe=False)
