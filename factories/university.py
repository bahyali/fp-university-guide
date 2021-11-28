import random
from flask_seeder import Faker
import app.models.university as model
from faker import Faker as FakeGenerator
from app.utilities.seeding import FakerIntegration as Generator

fake = FakeGenerator()

university_factory = Faker(
    cls=model.University,
    init={
        "name": Generator(lambda: '%s University' % fake.company()),
        "type": Generator(lambda: random.choice(['Public University', 'Private University'])),
        "about": Generator(lambda: fake.paragraph()),
        "location": Generator(lambda: '%s, %s' % (fake.country(), fake.city())),
        "logo": Generator(lambda: fake.image_url(200, 200).replace('lorempixel.com', 'loremflickr.com')),
    }
)

program_factory = Faker(
    cls=model.Program,
    init={
        "name": Generator(lambda: '%s Program' % fake.company()),
        "type": Generator(lambda: random.choice(['Undergraduate', 'Postgraduate'])),
        "about": Generator(lambda: fake.paragraph())
    }
)

scholarship_factory = Faker(
    cls=model.Scholarship,
    init={
        "name": Generator(lambda: '%s Scholarship' % fake.company()),
        "type": Generator(lambda: random.choice(['Undergraduate', 'Postgraduate'])),
        "about": Generator(lambda: fake.paragraph())
    }
)

campus_factory = Faker(
    cls=model.Campus,
    init={
        "name": Generator(lambda: '%s Campus' % fake.city()),
        "location": Generator(lambda: '%s, %s' % (fake.country(), fake.city())),
        "address": Generator(lambda: fake.address()),
    }
)

facility_factory = Faker(
    cls=model.Facility,
    init={
        "name": Generator(lambda: fake.word()),
        "image": Generator(lambda: fake.image_url(50, 50).replace('lorempixel.com', 'loremflickr.com')),
    }
)

contact_info_factory = Faker(
    cls=model.ContactInfo,
    init={
        "method": Generator(lambda: random.choice(['facebook', 'twitter', 'phone', 'instagram'])),
        "value": Generator(lambda: fake.url())
    }
)
