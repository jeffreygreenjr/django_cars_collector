from django.contrib import admin
from .models import Car # import the Artist model from models.py
from .models import Manufacturer
from .models import VehicleType
# Register your models here.

admin.site.register(Car) # this line will add the model to the admin panel
admin.site.register(Manufacturer)
admin.site.register(VehicleType)