import multiprocessing
from flask import url_for
from tests.rest_e2e.test_registration import create_user

multiprocessing.set_start_method("fork")


def test_website_running(live_server, selenium):
    selenium.get(url_for('app.index', _external=True))

    assert selenium.title == "Welcome to University Guide!"


def test_login(app, live_server, selenium):
    create_user(app)

    selenium.get(url_for('app.index', _external=True))

    login_btn = selenium.find_element_by_link_text('Login')
    login_btn.click()

    email_input = selenium.find_element_by_xpath("//input[@name='email']")
    email_input.send_keys("username@email.com")

    password_input = selenium.find_element_by_xpath("//input[@name='password']")
    password_input.send_keys("123456")

    button = selenium.find_element_by_xpath("//button[@type='submit']")
    button.click()

    assert selenium.title == "Welcome to University Guide!"
    assert selenium.find_element_by_class_name("navbar__auth__greeting").text == "Hello! firstname lastname"
