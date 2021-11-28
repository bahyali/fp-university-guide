from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash


def test_register(app, client):
    email = 'username@email.com'
    password = '123456'

    register(client, email, password)

    with app.app_context():
        user = User.query.filter_by(email=email).first()
    assert user.email == email
    assert check_password_hash(user.password, password)


def register(client, email, password):
    return client.post('/signup', data=dict(
        email=email,
        password=password,
        grade='first grade',
        first_name='firstname',
        last_name='lastname'
    ),
                       follow_redirects=True)


# ------- helpers ---------
def create_user(app):
    user: User = User(password=generate_password_hash('123456', method='sha256'),
                      email='username@email.com',
                      grade='first grade',
                      first_name='firstname',
                      last_name='lastname')

    # add the new user to the database
    with app.app_context():
        db.session.add(user)
        db.session.commit()
