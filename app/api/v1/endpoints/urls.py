"""
URL patterns for main endpoints.
"""

from django.urls import path

from . import views

urlpatterns = [
    path('health/', views.health, name='health'),
    path('settings/', views.settings, name='settings'),
]