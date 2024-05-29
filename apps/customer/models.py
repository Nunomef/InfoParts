# ./apps/customer/models.py

from django.db import models
from oscar.apps.customer.abstract_models import *


class Vehicle(models.Model):
    MODEL_CHOICES = [
        ('model1', 'Land Rover Series I'),
        ('model2', 'Land Rover Series II'),
        ('model3', 'Land Rover Series IIA'),
        ('model4', 'Land Rover Series III'),
        ('model5', 'Land Rover Defender 90'),
        ('model6', 'Land Rover Defender 110'),
        ('model7', 'Land Rover Defender 130'),
        ('model8', 'Land Rover Discovery'),
        ('model9', 'Land Rover Discovery Sport'),
        ('model10', 'Land Rover Freelander'),
        ('model11', 'Range Rover SE'),
        ('model12', 'Range Rover HSE'),
        ('model13', 'Range Rover Autobiography'),
        ('model14', 'Range Rover SVAAutobiography'),
        ('model15', 'Range Rover Sport SE'),
        ('model16', 'Range Rover Sport HSE'),
        ('model17', 'Range Rover Sport SVR'),
        ('model18', 'Range Rover Sport AutoBiography'),
        ('model19', 'Range Rover Evoque'),
        ('model20', 'Range Rover Velar'),
    ]

    DOORS_CHOICES = [
        (3, '3 doors'),
        (5, '5 doors'),
    ]

    FUEL_TYPE_CHOICES = [
        ('gasoline', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
    ]

    model = models.CharField(max_length=100, choices=MODEL_CHOICES)
    number_of_doors = models.IntegerField(choices=DOORS_CHOICES)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES)
    year = models.IntegerField()
    license_plate = models.CharField(
        max_length=8, unique=True)

    def __str__(self):
        return f"{self.model} ({self.license_plate})"


class UserVehicle(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'vehicle')



from oscar.apps.customer.models import *