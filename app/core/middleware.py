"""
Django middleware for request tracking and logging.
"""

import time
import uuid
import logging

from .logging import set_request_id

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """Middleware to add request ID and process time tracking."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Set request ID
        request.request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        
        # Set request ID in thread-local storage for logging
        set_request_id(request.request_id)
        
        # Record start time
        start_time = time.perf_counter()
        
        # Process the request
        response = self.get_response(request)
        
        # Calculate elapsed time
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        
        # Add headers to response
        response["X-Request-ID"] = request.request_id
        response["X-Process-Time-Ms"] = f"{elapsed_ms:.2f}"
        
        # Log the request
        logger.info(
            "Request processed",
            extra={
                "method": request.method,
                "path": request.path,
                "status_code": response.status_code,
                "process_time_ms": elapsed_ms,
            }
        )
        
        return response
