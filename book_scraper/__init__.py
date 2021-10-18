# Third part
from flask import Flask
from hashlib import md5 ### 0
from datetime import timedelta


def create_app() -> Flask:
    app = Flask(__name__)
    app.permanent_session_lifetime = timedelta(minutes=30)
    encryptor = md5()
    app.debug = True
    app.secret_key = encryptor.digest()
    # Blueprints
    from .server import SERVER_BLUEPRINT
    app.register_blueprint(SERVER_BLUEPRINT)

    return app