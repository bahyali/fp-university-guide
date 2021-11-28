import pytest
from app import create_app, db


@pytest.fixture
def app():
    app = create_app(
        {'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'postgresql://postgres:mysecretpassword@localhost/postgres'})

    """ Migrate database"""
    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
