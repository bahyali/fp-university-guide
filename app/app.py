from flask import Blueprint, render_template, url_for, request, flash, redirect
from markupsafe import escape
from flask_assets import Bundle
from dotenv import load_dotenv
from app.models.user import User
from app import login_manager, assets
from app.controllers.auth import SignupController, LoginController, ValidationException

load_dotenv()  # take environment variables from .env.

app = Blueprint('app', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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


@app.route('/login', methods=['POST'])
def authenticate():
    controller = LoginController(request.form)

    try:
        if controller.login():
            return redirect('/')

    except ValidationException as e:
        flash(str(e))
        return redirect(url_for('app.login'))  # if the user doesn't exist or password is wrong, reload the page


@app.route('/signup', methods=['GET'])
def signup():
    return render_template('%s/signup.html' % VIEWS_DIR)


@app.route('/signup', methods=['POST'])
def register():
    controller = SignupController(request.form)

    try:
        controller.register()
    except ValidationException as e:
        flash(str(e))

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


@app.route('/universities')
def show_universities():
    return 'University'


@app.route('/university/<int:uni_id>')
def show_university(uni_id):
    return 'University %d' % uni_id


@app.route('/scholarships')
def show_scholarships():
    return 'Scholarships'


@app.route('/scholarship/<int:scholarship_id>')
def show_scholarship(scholarship_id):
    return 'Scholarship %d' % scholarship_id


@app.route('/programs')
def show_programs():
    return 'Programs'


@app.route('/program/<int:program_id>')
def show_program(program_id):
    return 'Program %d' % program_id
