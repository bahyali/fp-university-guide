from app import db
from app.models.contact_item import ContactItem
from app.utilities.exceptions import ValidationException


class ContactUsController:
    def __init__(self, contact_data):
        self.contact_data = contact_data
        pass

    def add_contact_item(self):
        self.validate()

        contact_item = ContactItem(
            name=self.contact_data['name'],
            email=self.contact_data['email'],
            message=self.contact_data['message']
        )

        db.session.add(contact_item)
        db.session.commit()

        return contact_item

    def validate(self):
        required_fields = ['name', 'email', 'message']
        invalid_fields = []

        for field in required_fields:
            if not self.contact_data[field]:
                invalid_fields.append(field)

        if len(invalid_fields) > 0:
            raise ValidationException('All fields are required')
        pass
