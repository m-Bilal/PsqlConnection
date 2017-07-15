from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from web_app import models
from django.views.decorators.csrf import csrf_exempt
from web_app.models import Vehicle
from django.core import serializers
# Create your views here.

def hello(request):
    return HttpResponse("Hello")


@csrf_exempt
def add_data(request):
    # Check for POST request
    if request.method == 'POST':
        request_name = request.POST.get('name', '')
        request_id = request.POST.get('id', '')
        vehicle_instance = models.Vehicle.objects.create(name = request_name, id = request_id)
        return HttpResponse('success for %s', id)
    else:
        return HttpResponse('failed')

def get_all(request):
    a = dict()
    vehilces = list(Vehicle.objects.all())
    json_response = serializers.serialize('xml', Vehicle.objects.all())
    return HttpResponse(json_response)

