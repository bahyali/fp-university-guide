import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_assets import Environment, Bundle

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
login_manager = LoginManager()
assets = Environment()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') \
        .replace('postgres://', 'postgresql://')

    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    db.init_app(app)

    # Authenticator
    login_manager.login_view = 'app.login'
    login_manager.init_app(app)

    assets.init_app(app)
    # blueprint for non-auth parts of app
    from .app import app as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
