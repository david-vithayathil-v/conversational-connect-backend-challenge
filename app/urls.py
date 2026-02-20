"""
Main URL configuration for conversational-connect-backend.
"""

from django.contrib import admin
from django.urls import include, path

from app.core.config import get_settings

settings = get_settings()

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{settings.api_v1_prefix.lstrip("/")}/', include('app.api.v1.urls')),
]