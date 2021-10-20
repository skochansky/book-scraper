# Third part
from flask import Flask
from hashlib import md5
from datetime import timedelta


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config.Config")
    app.permanent_session_lifetime = timedelta(minutes=30)
    app.debug = True
    # Blueprints
    from .server import SERVER_BLUEPRINT
    app.register_blueprint(SERVER_BLUEPRINT)

    return app