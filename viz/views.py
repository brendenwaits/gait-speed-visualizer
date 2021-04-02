from django.shortcuts import render
from django.views.generic import ListView

from api.models import GaitMeasurement

class GaitMeasurementListView(ListView):
    queryset = GaitMeasurement.objects.order_by('-date')
    template_name = 'viz/gaitmeasurement_list.html'
