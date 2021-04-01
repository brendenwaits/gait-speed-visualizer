from rest_framework import serializers
from .models import GaitMeasurement

class GaitMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GaitMeasurement
        fields = ['speed' , 'date']
