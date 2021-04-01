from django.shortcuts import render
from rest_framework import viewsets

from .serializers import GaitMeasurementSerializer
from .models import GaitMeasurement

class GaitMeasurementViewSet(viewsets.ModelViewSet):
    queryset = GaitMeasurement.objects.all()
    serializer_class = GaitMeasurementSerializer
    permission_classes = []
