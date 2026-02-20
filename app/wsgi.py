"""
WSGI config for conversational-connect-backend.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from app.core.logging import configure_logging
from app.core.config import get_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# Configure logging early
settings = get_settings()
configure_logging(settings)

application = get_wsgi_application()