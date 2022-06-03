from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


class VehicleType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
        

class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.TextField(max_length=4)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="manufacturers")
    vehicletype = models.ManyToManyField(VehicleType)
    bio = models.TextField(max_length=500)
    img = models.CharField(max_length=500)
     # Add a relationship for the user
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

