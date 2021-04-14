"""
viz url definitions
"""
from django.urls import path

from viz.views import GaitVisualizationView

urlpatterns = [

    # /
    path('', GaitVisualizationView.as_view()),
]
