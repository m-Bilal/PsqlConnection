from django.db import models

# Create your models here.

# Model for vehicle
class Vehicle(models.Model):
    id = models.BigIntegerField(unique=True, null=False, primary_key=True)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    vehicle_type = models.IntegerField()
    name = models.CharField(max_length=100)
