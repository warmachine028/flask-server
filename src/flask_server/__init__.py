from importlib import metadata
from flask import Flask
from flask_server.routes import (
    health_bp,
    users_bp,
    error_bp,
    auth_bp
)

__version__ = metadata.version("flask_server")


def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(auth_bp)
    return app
