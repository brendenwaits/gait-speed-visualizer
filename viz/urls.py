"""
viz url definitions
"""
from django.urls import path

from viz.views import GaitMeasurementListView

urlpatterns = [

    # /
    path('', GaitMeasurementListView.as_view()),
]
