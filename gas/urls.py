from django.urls import path
from . import views
from .views import  GasListCreate, GasCreateView, GasList
app_name = "gas"

urlpatterns = [
    path('gas_list/',GasListCreate, name='gas-list'),
    path('gas_list/create/', GasCreateView, name='gas-create'),
    path('gas_list/<int:pk>/', views.GasRetrieveView.as_view(), name='gas-retrieve'),
    path('gas_list/<int:gas_id>/update/', views.GasUpdateView.as_view(), name='gas-update'),
    path('gas_list/<int:pk>/delete/', views.GasDeleteView.as_view(), name='gas-destroy'),
    path('user-gas/', GasList.as_view(), name='user-gas'),
]