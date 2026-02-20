from __future__ import annotations

import logging
import logging.config
import threading

from app.core.config import Settings

# Thread-local storage for request ID
_thread_locals = threading.local()


def set_request_id(request_id: str) -> None:
    """Set the request ID for the current thread."""
    _thread_locals.request_id = request_id


def get_request_id() -> str:
    """Get the request ID for the current thread."""
    return getattr(_thread_locals, 'request_id', '-')


class _RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:  # noqa: A003
        setattr(record, "request_id", get_request_id())
        return True


def configure_logging(settings: Settings) -> None:
    level = settings.log_level.upper()

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {"request_id": {"()": _RequestIdFilter}},
        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(levelname)s] request_id=%(request_id)s %(name)s: %(message)s"
            },
            "json": {
                "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "format": "%(asctime)s %(name)s %(levelname)s %(request_id)s %(message)s"
            }
        },
        "handlers": {
            "default": {
                "level": level,
                "formatter": settings.log_format if settings.log_format in ["json", "standard"] else "standard",
                "filters": ["request_id"],
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "root": {"handlers": ["default"], "level": level},
    }

    logging.config.dictConfig(logging_config)

