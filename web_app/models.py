from django.db import models

# Create your models here.

# Model for vehicle
class Vehicle(models.Model):
    id = models.BigIntegerField(unique=True, null=False, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name