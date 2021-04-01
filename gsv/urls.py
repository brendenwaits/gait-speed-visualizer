"""
gsv url definitions
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('api.urls')),

    # /admin/
    path('admin/', admin.site.urls),
]
