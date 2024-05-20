# accounts/urls.py

from django.urls import path
from .views import register_user, user_login, user_logout, user_list,  request_password_reset, reset_password, AddressCreateView, AddressListCreate, AddressRetrieveView, AddressUpdateView, AddressDeleteView, KycListCreate, KycCreateView, KycRetrieveView, KycDeleteView, kyc_update_view, change_password

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('cat/', user_logout, name='logout'),
    path('users/', user_list, name='user-list'),
    path('password/change/', change_password, name='change_password'),
    path('password/reset/', request_password_reset, name='password_reset'),
    path('password/reset/<uidb64>/<token>/', reset_password, name='password_reset_confirm'),
    path('kyc_list/', KycListCreate, name='kyc-list'),
    path('kyc/create/', KycCreateView, name='kyc-create'),
    path('kyc_detail/<int:pk>/', KycRetrieveView.as_view(), name='kyc_detail'),
    path('kyc-update/<int:user_id>/', kyc_update_view, name='kyc_update'),
    path('kyc/<int:pk>/delete/', KycDeleteView.as_view(), name='kyc-destroy'),
    path('address_list/', AddressListCreate, name='service-list'),
    path('address/create/', AddressCreateView, name='address-create'),
    path('addresss_detail/<int:pk>/', AddressRetrieveView.as_view(), name='address_detail'),
    path('address_list/<int:address_id>/update/', AddressUpdateView.as_view(), name='address-update'),
    path('address/<int:pk>/delete/', AddressDeleteView.as_view(), name='address-destroy'),

]