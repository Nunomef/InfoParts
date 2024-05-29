# ./apps/customer/urls.py

from django.urls import path
from .views import VehicleListView, VehicleCreateView, VehicleUpdateView, VehicleDeleteView

app_name = 'my_customer'

urlpatterns = [
    path('vehicles/', VehicleListView.as_view(), name='vehicle_list'),
    path('vehicles/add/', VehicleCreateView.as_view(), name='vehicle_add'),
    path('vehicles/<int:pk>/edit/', VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('vehicles/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),
]