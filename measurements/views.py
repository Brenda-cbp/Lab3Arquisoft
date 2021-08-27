from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic import logic_measurement

# Create your views here.
def get_measurements(request):
    measurements = logic_measurement.get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type='application/json')

def get_measurement(request, id):
    measurement = logic_measurement.get_measurement(id)
    measurement_rta= serializers.serialize('json', measurement)
    return HttpResponse(measurement_rta, content_type='application/json')

def delete_measurement(request, id):
    return HttpResponse(logic_measurement.delete_measurement(id))

def update_measurement(request,id):
    measurement = logic_measurement.update_measurement(id, "value", 11500 )
    measurement_rta= serializers.serialize('json', measurement)
    return HttpResponse(measurement_rta, content_type='application/json');