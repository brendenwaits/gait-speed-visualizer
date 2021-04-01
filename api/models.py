from django.db import models

class GaitMeasurement(models.Model):
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField()
