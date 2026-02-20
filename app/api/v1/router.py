from flask import Blueprint

from app.api.v1.endpoints.main import bp as main_bp

api_v1 = Blueprint("api_v1", __name__)
api_v1.register_blueprint(main_bp)
