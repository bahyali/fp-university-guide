from test_auth import login
from test_registration import create_user
from urllib.parse import urlparse


def test_redirect_if_authenticated(app, client):
    create_user(app)
    login(client, 'username@email.com', '123456')

    rv = client.get('/login', follow_redirects=False)

    assert rv.status_code == 302
    assert urlparse(rv.location).path == "/"
