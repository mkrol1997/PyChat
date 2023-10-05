from datetime import timedelta
from hashlib import md5

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from chatapp.constants import DB_PATH
from chatapp.ws_events import socketio

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    encryptor = md5()

    app.permanent_session_lifetime = timedelta(minutes=30)
    app.config['SECRET_KEY'] = encryptor.digest()
    app.config['DEBUG'] = True

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    socketio.init_app(app)

    app.debug = True
    from chatapp.web_app import main
    app.register_blueprint(main)

    return app
