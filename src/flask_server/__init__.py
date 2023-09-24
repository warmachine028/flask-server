from importlib import metadata
from flask import Flask
from flask_server.routes.health import health_bp
from flask_server.routes.users import users_bp
from flask_server.routes.error import error_bp

__version__ = metadata.version("flask_server")


def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    return app
