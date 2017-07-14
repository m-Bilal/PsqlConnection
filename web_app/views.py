from django.shortcuts import render
from django.http import HttpResponse
from web_app import models

# Create your views here.

def hello(request):
    return HttpResponse("Hello")

def add_data(request):
    # Check for POST request
    if request.method == 'POST':
        request_name = request.POST.get('name', '')
        request_id = request.POST.get('id', '')
        vehicle_instance = models.Vehicle.objects.create(name = request_name, id = request_id)
        return 'success for %s', id

