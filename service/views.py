from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Service, Device
from .serializers import ServiceSerializer,DeviceSerializer, ThirdUserSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAuthenticated
import datetime

class DeviceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

@api_view(['GET'])
def DeviceListCreate(request):
    if request.method == 'GET':
        device = Device.objects.all()
        serializer = DeviceSerializer(device, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def ServiceCreateView(request):
    if request.method == 'POST':
        service_serializer = ServiceSerializer(data=request.data)
        # Check if Service_getter exists in request data
        if request.data.get('Service_getter') != "me":
            third_user_data = {
                'user': request.user.id,
                'name': request.data.get('Service_getter'),
                'contact': request.data.get('contact'),
                'alternativ_number': request.data.get('alternativ_number'),
                'province': request.data.get('province'),
                'district': request.data.get('district'),
                'municipality': request.data.get('municipality'),
                'wada': request.data.get('wada'),
                'tole': request.data.get('tole'),
                'zipcode': request.data.get('zipcode'),
                'landmark': request.data.get('landmark'),
            }
            

            # Create serializer instances for both models
            third_user_serializer = ThirdUserSerializer(data=third_user_data)
            if third_user_serializer.is_valid():
                # Save the ThirdUser instance
                third_user_serializer.save()
            else:
                return Response(third_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        

        if service_serializer.is_valid():
            
            service_serializer.save()
            return Response(service_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
         

@api_view(['GET'])
def ServiceListView(request):
    if request.method == 'GET':
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ServiceRetrieveView(APIView):
    def get(self, request, pk):
        try:
            service = Service.objects.get(id=pk)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ServiceUpdateView(UpdateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_url_kwarg = 'service_id' 

class ServiceDeleteView(DestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()




class UserServicesAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Service.objects.filter(user=self.request.user)
        else:
            return Service.objects.none()  #
    
