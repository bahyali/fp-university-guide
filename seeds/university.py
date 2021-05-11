import random

from flask_seeder import Seeder, Faker
import app.models.university as model

from faker import Faker as FakeGenerator
from app.utilities.seeding import FakerIntegration as Generator

fake = FakeGenerator()


class UniversitySeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        university_faker = Faker(
            cls=model.University,
            init={
                "name": Generator(lambda: '%s University' % fake.company()),
                "type": Generator(lambda: random.choice(['Public University', 'Private University'])),
                "about": Generator(lambda: fake.paragraph()),
                "location": Generator(lambda: '%s, %s' % (fake.country(), fake.city())),
                "logo": Generator(lambda: fake.image_url(200, 200).replace('lorempixel.com', 'loremflickr.com')),
            }
        )

        program_faker = Faker(
            cls=model.Program,
            init={
                "name": Generator(lambda: '%s Program' % fake.company()),
                "type": Generator(lambda: random.choice(['Undergraduate', 'Postgraduate'])),
                "about": Generator(lambda: fake.paragraph())
            }
        )

        scholarship_faker = Faker(
            cls=model.Scholarship,
            init={
                "name": Generator(lambda: '%s Scholarship' % fake.company()),
                "type": Generator(lambda: random.choice(['Undergraduate', 'Postgraduate'])),
                "about": Generator(lambda: fake.paragraph())
            }
        )

        campus_faker = Faker(
            cls=model.Campus,
            init={
                "name": Generator(lambda: '%s Campus' % fake.city()),
                "location": Generator(lambda: '%s, %s' % (fake.country(), fake.city())),
                "address": Generator(lambda: fake.address()),
            }
        )

        facility_faker = Faker(
            cls=model.Facility,
            init={
                "name": Generator(lambda: fake.word()),
                "image": Generator(lambda: fake.image_url(50, 50).replace('lorempixel.com', 'loremflickr.com')),
            }
        )

        contact_info_faker = Faker(
            cls=model.ContactInfo,
            init={
                "method": Generator(lambda: random.choice(['facebook', 'twitter', 'phone', 'instagram'])),
                "value": Generator(lambda: fake.url())
            }
        )

        # Create
        for uni in university_faker.create(5):
            for program in program_faker.create(random.randint(1, 5)):
                uni.programs.append(program)

            for scholarship in scholarship_faker.create(random.randint(1, 5)):
                uni.scholarships.append(scholarship)

            for campus in campus_faker.create(random.randint(1, 5)):
                for facility in facility_faker.create(random.randint(1, 5)):
                    campus.facilities.append(facility)
                uni.campuses.append(campus)

            for contact_info in contact_info_faker.create(random.randint(1, 5)):
                uni.contact_info.append(contact_info)

            print("Adding University: %s" % uni)
            self.db.session.add(uni)
