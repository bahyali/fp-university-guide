from app import db
from app.models.contact_item import ContactItem


def test_add_contact_us_item(app):
    payload = {
        "name": "Bahy",
        "email": 'bahy@code.berlin',
        "message": 'Good Message'
    }
    with app.app_context():
        add_item(payload)

        items = ContactItem.query.filter_by(email=payload['email'], message=payload['message']).all()

    assert len(items) == 1
    assert items[0].email == payload['email']
    assert items[0].message == payload['message']


def add_item(payload):
    contact_item = ContactItem(**payload)
    db.session.add(contact_item)
    db.session.commit()
