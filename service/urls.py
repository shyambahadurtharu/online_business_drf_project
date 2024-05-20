from django.urls import path
from . import views
from .views import DeviceListCreate, DeviceRetrieveUpdateDestroy, ServiceListView, ServiceCreateView, UserServicesAPIView,ServiceRetrieveView
app_name = "service"

urlpatterns = [
    path('e_devices/', DeviceListCreate, name='devices-list'),
   
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroy.as_view(), name='device-detail'),
    path('service_list/', ServiceListView, name='service-list'),
    path('service/create/', ServiceCreateView, name='service-create'),
    path('services_detail/<int:pk>/', ServiceRetrieveView.as_view(), name='service_detail'),
    path('service_list/<int:service_id>/update/', views.ServiceUpdateView.as_view(), name='service-update'),
    path('service/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service-destroy'),
    path('user-services/', UserServicesAPIView.as_view(), name='user-services'),
]