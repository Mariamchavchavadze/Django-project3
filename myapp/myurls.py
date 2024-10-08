# myapp/urls.py
from django.urls import path
from .views import vehicle_list, add_vehicle, vehicle_detail

urlpatterns = [
    path('', vehicle_list, name='vehicle_list'),
    path('add/', add_vehicle, name='add_vehicle'),
    path('detail/<int:vehicle_id>/', vehicle_detail, name='vehicle_detail'),
]

