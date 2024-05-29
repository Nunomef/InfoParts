# ./apps/customer/views.py

from django.views import View
from django.shortcuts import render, redirect
from .forms import VehicleForm, UserVehicleForm
from .models import Vehicle, UserVehicle
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class VehicleListView(View):
    def get(self, request):
        vehicles = UserVehicle.objects.filter(user=request.user)
        return render(request, 'oscar/customer/vehicles/vehicle_list.html', {'vehicles': vehicles})


@method_decorator(login_required, name='dispatch')
class VehicleCreateView(View):
    def get(self, request):
        form = VehicleForm()
        return render(request, 'oscar/customer/vehicles/vehicle_form.html', {'form': form})

    def post(self, request):
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save()
            UserVehicle.objects.create(user=request.user, vehicle=vehicle)
            messages.success(request, 'Vehicle added successfully.')
            return redirect('my_customer:vehicle_list')  # change this line
        return render(request, 'oscar/customer/vehicles/vehicle_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class VehicleUpdateView(View):
    def get(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        form = VehicleForm(instance=vehicle)
        return render(request, 'oscar/customer/vehicles/vehicle_form.html', {'form': form, 'is_edit': True})

    def post(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle updated successfully.')
            return redirect('my_customer:vehicle_list')  # change this line
        return render(request, 'oscar/customer/vehicles/vehicle_form.html', {'form': form, 'is_edit': True})


@method_decorator(login_required, name='dispatch')
class VehicleDeleteView(View):
    def get(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        return render(request, 'oscar/customer/vehicles/vehicle_confirm_delete.html', {'vehicle': vehicle})

    def post(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        user_vehicle = UserVehicle.objects.get(user=request.user, vehicle=vehicle)
        vehicle.delete()
        user_vehicle.delete()
        messages.success(request, 'Vehicle deleted successfully.')
        return redirect('my_customer:vehicle_list')  # change this line


from oscar.apps.customer.views import *