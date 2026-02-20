"""
API v1 endpoint views.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.api.v1.services.main import BackendService


@api_view(['GET'])
def health(request):
    """Health check endpoint."""
    return Response({"status": "ok"})


@api_view(['GET'])
def settings(request):
    """Settings endpoint."""
    backend_service = BackendService()
    return Response(backend_service.get_settings())