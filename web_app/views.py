from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from web_app import models
from django.views.decorators.csrf import csrf_exempt
from web_app.models import Vehicle
from django.core import serializers
from web_app import serializers as web_app_serializers
from collections import defaultdict
from django.db.models.query import QuerySet
import json
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
    json_response = serializers.serialize('json', Vehicle.objects.all())
    a = dict()
    a['value1'] = 1
    a['value2'] = 2
    return HttpResponse('{\"values\":' + json_response + '}', content_type='application/json')

