from app.controllers.university import UniversityController


def test_empty_db(app):
    """Start with a blank database."""
    with app.app_context():
        result = UniversityController.index()

    assert result['universities'] == []


def test_app_working(client):
    assert client.get('/').status_code == 200


def test_404(client):
    assert client.get('/404').status_code == 404
