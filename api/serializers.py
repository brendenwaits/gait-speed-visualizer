from rest_framework import serializers
from datetime import datetime

from .models import GaitMeasurement

class GaitMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    date = serializers.DateTimeField(
        required=False,
        default=datetime.now()
    )

    class Meta:
        model = GaitMeasurement
        fields = ['speed' , 'date']
