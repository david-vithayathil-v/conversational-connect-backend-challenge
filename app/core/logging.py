from __future__ import annotations

import logging
import logging.config

from app.core.config import Settings

try:
    from flask import g, has_request_context
except Exception:  # pragma: no cover
    g = None

    def has_request_context() -> bool:  # type: ignore[no-redef]
        return False


class _RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:  # noqa: A003
        request_id = "-"
        if has_request_context() and g is not None:
            request_id = getattr(g, "request_id", "-")
        setattr(record, "request_id", request_id)
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
            }
        },
        "handlers": {
            "default": {
                "level": level,
                "formatter": "standard",
                "filters": ["request_id"],
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "root": {"handlers": ["default"], "level": level},
    }

    logging.config.dictConfig(logging_config)

