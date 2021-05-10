from flask import Flask, render_template, url_for
from markupsafe import escape
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

# Static assets
assets = Environment(app)
assets.url = app.static_url_path
# assets.debug = True

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


@app.route('/')
def hello_world():
    return render_template('%s/hello.html' % VIEWS_DIR)


@app.route('/style_guide')
def style_guide():
    return render_template('%s/cards.html' % STYLEGUIDE_DIR)


@app.route('/style_guide/<path:subpath>')
def style_guide_subpath(subpath):
    # show the subpath after /path/
    return render_template('%s/%s.html' % (STYLEGUIDE_DIR, escape(subpath)))


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User1 %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
