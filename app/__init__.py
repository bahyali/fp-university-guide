import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from flask_login import LoginManager
from flask_assets import Environment
from flask_seeder import FlaskSeeder

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
seeder = FlaskSeeder()
migrate = Migrate()

login_manager = LoginManager()
ma = Marshmallow()
assets = Environment()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') \
        .replace('postgres://', 'postgresql://')

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # Stop caching static files in dev
    if os.environ.get('FLASK_ENV') == 'development':
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    if test_config:
        app.config.update(test_config)

    # Database stuff
    db.init_app(app)
    migrate.init_app(app, db)
    seeder.init_app(app, db)
    ma.init_app(app)

    # Authenticator
    login_manager.login_view = 'app.login'
    login_manager.init_app(app)

    assets.init_app(app)
    # blueprint for non-auth parts of app
    from .app import app as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
