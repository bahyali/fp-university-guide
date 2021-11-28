from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash


# Registration
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


def test_register(app, client):
    pass


def register(client, email, password):
    return client.post('/login', data=dict(email=email, password=password),
                       follow_redirects=True)
