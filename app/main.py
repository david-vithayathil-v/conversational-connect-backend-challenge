from __future__ import annotations

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from app.api.v1.router import api_v1
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.core.middleware import init_request_context


def create_app() -> Flask:
    settings = get_settings()
    configure_logging(settings)

    app = Flask(__name__)
    app.register_blueprint(api_v1, url_prefix=settings.api_v1_prefix)
    init_request_context(app)

    @app.errorhandler(HTTPException)
    def handle_http_exception(exc: HTTPException):
        return (
            jsonify(
                {
                    "error": {
                        "type": "http_error",
                        "message": exc.description,
                        "status_code": exc.code,
                    }
                }
            ),
            exc.code,
        )

    @app.errorhandler(Exception)
    def handle_unhandled_exception(exc: Exception):
        return (
            jsonify(
                {
                    "error": {
                        "type": "internal_error",
                        "message": "Unhandled server error",
                    }
                }
            ),
            500,
        )

    return app


app = create_app()
