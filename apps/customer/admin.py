# apps/customer/admin.py

from django.contrib import admin
from .models import Vehicle, UserVehicle

admin.site.register(Vehicle)
admin.site.register(UserVehicle) 