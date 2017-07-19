from rest_framework import serializers
from web_app import models as web_app_models


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = web_app_models.Vehicle
        #fields = ('id', 'name')
        fields = '__all__'
