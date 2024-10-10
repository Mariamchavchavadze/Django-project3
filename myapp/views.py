# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'myapp/vehicle_list.html', {'vehicles': vehicles})


# myapp/views.py

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'myapp/add_vehicle.html', {'form': form})


def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    return render(request, 'myapp/vehicle_detail.html', {'vehicle': vehicle})


def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'myapp/delete_vehicle.html', {'vehicle': vehicle})
