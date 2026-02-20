from __future__ import annotations

import time
import uuid

from flask import Flask, g, request


def init_request_context(app: Flask) -> None:
    @app.before_request
    def _before_request() -> None:
        g.request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        g._start_time = time.perf_counter()

    @app.after_request
    def _after_request(response):
        elapsed_ms = (time.perf_counter() - getattr(g, "_start_time", time.perf_counter())) * 1000
        response.headers["X-Request-ID"] = getattr(g, "request_id", "-")
        response.headers["X-Process-Time-Ms"] = f"{elapsed_ms:.2f}"
        return response
