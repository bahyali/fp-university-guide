from app.controllers.auth import LoginController
from app.models.user import User
from werkzeug.security import generate_password_hash
from pytest import raises

from app.utilities.exceptions import ValidationException


def test_check_credentials_valid(mocker):
    payload = {
        'email': 'bahy@test.com',
        'password': '123456'
    }

    con = LoginController(payload)
    mock_model = mocker.patch('app.controllers.auth.User')
    mock_model.query.filter_by \
        .return_value.first.return_value = User(email=payload['email'],
                                                password=generate_password_hash(payload['password']))
    try:
        con.check_credentials()
    except:
        assert False, f'Raised an exception'


def test_check_credentials_wrong_password(mocker):
    payload = {
        'email': 'bahy@test.com',
        'password': '123456'
    }

    con = LoginController(payload)
    mock_model = mocker.patch('app.controllers.auth.User')
    mock_model.query.filter_by \
        .return_value.first.return_value = User(email=payload['email'],
                                                password=generate_password_hash('123'))
    with raises(ValidationException):
        con.check_credentials()
