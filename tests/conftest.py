import pytest
from app import create_app, db


def determine_scope(fixture_name, config):
    if config.getoption("--driver", "Chrome"):
        return "session"
    return "function"


@pytest.fixture(scope=determine_scope)
def app():
    app = create_app(
        {
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///temp.db'
        }
    )

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
