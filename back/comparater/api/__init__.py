from flask import Blueprint
from flask_restful import Api

from models.database import db

from .golds import Golds,Gold

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


def register_api(app):
    @api_bp.before_request
    def before_request():
        db.connect(reuse_if_open=True)

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()

    api.add_resource(Golds, '/golds')
    api.add_resource(Gold, '/gold/<gold_name>')

    app.register_blueprint(api_bp, url_prefix="/api/v1")
