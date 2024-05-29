# ./apps/customer/forms.py

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import re
from .models import Vehicle, UserVehicle
from django.contrib.auth import get_user_model

User = get_user_model()

def validate_license_plate(value):
    # Check if the license plate has the correct format
     if not re.match(r'^([A-Z]{2}-\d{2}-[A-Z]{2}|\d{2}-[A-Z]{2}-\d{2}|\d{2}-\d{2}-\d{2}|[A-Z]{2}-\d{2}-\d{2}|[A-Z]{2}-[A-Z]{2}-[A-Z]{2}|\d{2}-\d{2}-[A-Z]{2})$', value):
        raise ValidationError(
            _('%(value)s is not a valid license plate'),
            params={'value': value},
        )

class VehicleForm(forms.ModelForm):
    YEAR_CHOICES = [(r,r) for r in range(1948, timezone.now().year+1)]
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    license_plate = forms.CharField(validators=[validate_license_plate])
    
    class Meta:
        model = Vehicle
        fields = ['model', 'number_of_doors', 'fuel_type', 'year', 'license_plate']

class UserVehicleForm(forms.ModelForm):
    class Meta:
        model = UserVehicle
        fields = ['user', 'vehicle']
        widgets = {'user': forms.HiddenInput()}
        
from oscar.apps.customer.forms import *