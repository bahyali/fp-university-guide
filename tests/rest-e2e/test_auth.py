from test_registration import create_user

login_error_message = b'Please check your login details and try again'


def test_login(app, client):
    create_user(app)

    rv = login(client, 'username@email.com', '123456')

    assert rv.status_code == 200
    assert login_error_message not in rv.data
    assert b"Hello! firstname lastname" in rv.data


def test_failed_login_wrong_email(app, client):
    create_user(app)

    rv = login(client, 'wrong_email@email.com', '123456')

    assert login_error_message in rv.data


def test_failed_login_wrong_password(app, client):
    create_user(app)

    rv = login(client, 'username@email.com', 'wrong_password')

    assert login_error_message in rv.data


def test_logout(app, client):
    create_user(app)

    login(client, 'username@email.com', '123456')
    rv = logout(client)

    assert rv.status_code == 200
    assert b"Login" in rv.data


# ------------- helpers ------------ #


def login(client, email, password):
    return client.post('/login', data=dict(email=email, password=password),
                       follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)
