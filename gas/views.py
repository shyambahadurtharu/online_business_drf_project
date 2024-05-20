from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Gas
from .serializers import GasSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAuthenticated
from service.serializers import ThirdUserSerializer



@api_view(['GET'])
def GasListCreate(request):
    if request.method == 'GET':
        device = Gas.objects.all()
        serializer = GasSerializer(device, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GasList(generics.ListAPIView):
    serializer_class = GasSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Gas.objects.filter(user=self.request.user)
        else:
            return Gas.objects.none()  #



@api_view(['POST'])
def GasCreateView(request):
    if request.method == 'POST':
        serializer = GasSerializer(data=request.data)
        if request.data.get('Service_getter') != "me":
            third_user_data = {
                'user': request.user.id,
                'name': request.data.get('Service_getter'),
                'contact': request.data.get('contact'),
                'adress': request.data.get('address'),
            }

            # Create serializer instances for both models
            third_user_serializer = ThirdUserSerializer(data=third_user_data)
            if third_user_serializer.is_valid():
                # Save the ThirdUser instance
                third_user_serializer.save()
            else:
                return Response(third_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GasRetrieveView(APIView):
    def get(self, request, pk):
        try:
            gas = Gas.objects.get(id=pk)
        except Gas.DoesNotExist:
            return Response({"error": "Gas not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = GasSerializer(gas)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GasUpdateView(UpdateAPIView):
    serializer_class = GasSerializer
    queryset = Gas.objects.all()
    lookup_url_kwarg = 'gas_id' 

class GasDeleteView(DestroyAPIView):
    serializer_class = GasSerializer
    queryset = Gas.objects.all()
