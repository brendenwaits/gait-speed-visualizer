"""
api url definitions
"""
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'gaitmeasurements', views.GaitMeasurementViewSet)

urlpatterns = [

    # /api/
    path('api/', include(router.urls)),

    #/api-auth/
    path('api-auth/', include('rest_framework.urls'))
]
