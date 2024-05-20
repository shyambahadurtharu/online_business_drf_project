from django.urls import path
from . import views
app_name = "address"
urlpatterns = [
    path('provinces/', views.get_province, name='get_province'),
    path('districts/<int:province_id>/', views.get_districts, name='get_districts'),
    path('municipalities/<int:district_id>/', views.get_municipalities, name='get_municipalities'),
]