# accounts/views.py

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import  UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, AddressSerializer, KycSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout, login
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser, Address, KycUser
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.template.response import TemplateResponse



@api_view(['POST'])
def register_user(request):
   
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Check if username or email already exist
            username = serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')
            if CustomUser.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if CustomUser.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            user_id = user.id
            kyc = {
                'user': user_id,
                
            }
            kycuser_serializer = KycSerializer(data=kyc)
            if kycuser_serializer.is_valid():
                # Save the ThirdUser instance
                kycuser_serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@api_view(['POST'])
def user_logout(request):
    if request.method == 'POST':
       
        logout(request)
        
        # Retrieve the token from the Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({'error': 'Authorization header missing'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Extract token from the header
        token_key = extract_token_from_header(auth_header)

        if not token_key:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        # Retrieve the token object
        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            # Token does not exist, handle the error
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        # Delete the user's token to logout
        token.delete()
        
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
    else:
        # Method not allowed
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def extract_token_from_header(auth_header):
    """
    Extract token from Authorization header.
    """
    auth_type, token = auth_header.split(' ')
    if auth_type.lower() != 'token':
        return None
    return token

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
   
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def request_password_reset(request):
    if request.method == 'POST':
        email = request.data.get('email')
        print(email)
        try:
            user = CustomUser.objects.get(email=email)
           
        except CustomUser.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Generate reset token
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        
        # Send password reset email
        reset_link = request.build_absolute_uri(reverse('password_reset_confirm', args=[uidb64, token]))
       
        subject = 'Password Reset Request'
        message = f'Use the following link to reset your password: {reset_link}'
        send_mail(subject, message, 'codebloominfotech@gmail.com', [email])
        
        return Response({'message': 'Password reset link sent to your email.'}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def reset_password(request, uidb64, token):
    if request.method == 'GET':
        try:
            uid = str(urlsafe_base64_decode(uidb64), 'utf-8')
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            # Assuming you want to render an appropriate template or return a valid response for the frontend to handle
            context = {'uidb64': uidb64, 'token': token}
            return TemplateResponse(request, 'reset_password.html', context)
        else:
            return Response({'error': 'Invalid password reset link.'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        try:
            uid = str(urlsafe_base64_decode(uidb64), 'utf-8')
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            return Response({'error': 'Invalid link.'}, status=status.HTTP_400_BAD_REQUEST)

        if user is not None and default_token_generator.check_token(user, token):
            new_password = request.data.get('new_password')
            user.set_password(new_password)
            user.save()
            context={
                'redirect_url':'http://localhost:3000/',
            }
            return TemplateResponse(request, 'password_success.html', context)
        else:
            return Response({'error': 'Invalid password reset link.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    # Check if the old password provided matches the current password of the user
    if not user.check_password(old_password):
        return Response({'error': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

    # Set the new password for the user
    user.set_password(new_password)
    user.save()

    return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)

    
@api_view(['GET'])
def KycListCreate(request):
    if request.method == 'GET':
        kyc = KycUser.objects.all()
        serializer = KycSerializer(kyc, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def KycCreateView(request):
    if request.method == 'POST':
        kyc_serializer = KycSerializer(data=request.data)                
        
        if kyc_serializer.is_valid():
            
            kyc_serializer.save()
            return Response(kyc_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(kyc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
# @permission_classes([IsAuthenticated])
@api_view(['PUT'])
def kyc_update_view(request, user_id):
    user = request.user
    try:
        user = KycUser.objects.get(user=user_id)
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = KycSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KycRetrieveView(APIView):
    def get(self, request, pk):
        try:
            address = KycUser.objects.get(id=pk)
        except KycUser.DoesNotExist:
            return Response({"error": "Information not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = KycSerializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class KycDeleteView(DestroyAPIView):
    serializer_class = KycSerializer
    queryset = KycUser.objects.all()


@api_view(['GET'])
def AddressListCreate(request):
    if request.method == 'GET':
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def AddressCreateView(request):
    if request.method == 'POST':
        address_serializer = AddressSerializer(data=request.data)                
        
        if address_serializer.is_valid():
            
            address_serializer.save()
            return Response(address_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AddressRetrieveView(APIView):
    def get(self, request, pk):
        try:
            address = Address.objects.get(id=pk)
        except Address.DoesNotExist:
            return Response({"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddressSerializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AddressUpdateView(UpdateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    lookup_url_kwarg = 'address_id' 

class AddressDeleteView(DestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

