"""
gsv url definitions
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # /admin/
    path('admin/', admin.site.urls),
]
