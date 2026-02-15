import logging
import logging.config


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] - %(pathname)s:%(lineno)d - %(name)s: %(message)s"
        }
    },
    "handlers": {
        "default": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "": {"handlers": ["default"], "level": "WARNING", "propagate": False},
        "conversational_connect_backend_test": {
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False,
        },
        "__main__": {"handlers": ["default"], "level": "DEBUG", "propagate": False},
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("conversational_connect_backend_test")

