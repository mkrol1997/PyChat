from datetime import timedelta
from hashlib import md5

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

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

    login_manager = LoginManager(app)

    from chatapp.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from chatapp.main import main
    app.register_blueprint(main)

    from chatapp.auth import auth
    app.register_blueprint(auth)

    return app
