from django.db import models
from oscar.apps.partner.abstract_models import AbstractPartner

class Partner(AbstractPartner):    
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)

from oscar.apps.partner.models import * 
