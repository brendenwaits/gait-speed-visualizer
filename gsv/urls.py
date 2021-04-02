"""
gsv url definitions
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # /
    path('', include('viz.urls')),

    # /api
    path('api/', include('api.urls')),

    # /admin/
    path('admin/', admin.site.urls),
]
