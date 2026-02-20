from __future__ import annotations

from flask import Blueprint, jsonify

from app.api.v1.services.main import BackendService

bp = Blueprint("main", __name__)


@bp.get("/health")
def health():
    return jsonify({"status": "ok"})


@bp.get("/settings")
def settings():
    backend_service = BackendService()
    return jsonify(backend_service.get_settings())
