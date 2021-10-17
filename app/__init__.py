# Third part
from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Blueprints
    from .server import SERVER_BLUEPRINT
    app.register_blueprint(SERVER_BLUEPRINT)

    return app