"""
Django application entry point.
"""

import os
import sys
from pathlib import Path

import django
from django.conf import settings
from django.core.management import execute_from_command_line

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

def run_server():
    """Run Django development server."""
    django.setup()
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])

if __name__ == '__main__':
    run_server()


app = create_app()
