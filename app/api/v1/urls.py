"""
URL configuration for API v1.
"""

from django.urls import include, path

urlpatterns = [
    path('', include('app.api.v1.endpoints.urls')),
]