from pytest import raises
from app.controllers.contact_us import ContactUsController
from app.utilities.exceptions import ValidationException


def test_invalid_message():
    bad_payload = {
        "name": "Bahy Ali",
        "email": 'test@tes.com',
        "message": ''
    }

    con = ContactUsController(bad_payload)

    with raises(ValidationException):
        con.validate()


def test_invalid_name():
    bad_payload = {
        "name": "",
        "email": 'test@tes.com',
        "message": 'Good Message'
    }

    con = ContactUsController(bad_payload)

    with raises(ValidationException):
        con.validate()


def test_invalid_email():
    bad_payload = {
        "name": "Bahy",
        "email": '',
        "message": 'Good Message'
    }

    con = ContactUsController(bad_payload)

    with raises(ValidationException):
        con.validate()


def test_valid_input():
    bad_payload = {
        "name": "Bahy",
        "email": 'bahy@code.berlin',
        "message": 'Good Message'
    }

    con = ContactUsController(bad_payload)

    try:
        con.validate()
    except:
        assert False
