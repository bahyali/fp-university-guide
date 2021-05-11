import os
from flask import Flask, render_template, url_for
from markupsafe import escape
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import LoginManager

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# Authenticator
# login_manager = LoginManager()
# login_manager.init_app(app)

# Static assets
assets = Environment(app)
assets.url = app.static_url_path

# Website
website_scss = Bundle('sass/base.scss', depends='sass/**/*.scss', filters='scss', output='css/styles.css')
assets.register('scss_all', website_scss)

# Style Guide
style_guide_scss = Bundle('style_guide/sass/base.scss', depends='style_guide/sass/*.scss', filters='scss',
                          output='style_guide/css/styles.css')
assets.register('sg_scss_all', style_guide_scss)

# Constants
VIEWS_DIR = 'views'
STYLEGUIDE_DIR = 'views/style_guide'


# Routes

@app.route('/')
def hello_world():
    return render_template('%s/hello.html' % VIEWS_DIR)


@app.route('/login')
def login():
    return render_template('%s/login.html' % VIEWS_DIR)


@app.route('/signup')
def signup():
    return render_template('%s/signup.html' % VIEWS_DIR)


@app.route('/style_guide')
def style_guide():
    return render_template('%s/index.html' % STYLEGUIDE_DIR)


@app.route('/style_guide/<path:subpath>')
def style_guide_subpath(subpath):
    return render_template('%s/%s.html' % (STYLEGUIDE_DIR, escape(subpath)))


@app.route('/blog')
def show_blog():
    return 'Blog'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/university')
def show_universities():
    return 'University'


@app.route('/university/<int:uni_id>')
def show_university(uni_id):
    return 'University %d' % uni_id


@app.route('/program')
def show_programs():
    return 'Programs'


@app.route('/program/<int:program_id>')
def show_program(program_id):
    return 'Program %d' % program_id
