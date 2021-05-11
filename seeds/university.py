import random

from flask_seeder import Seeder, Faker, generator
import app.models.university as model


class UniversitySeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        university_faker = Faker(
            cls=model.University,
            init={
                "name": generator.Name(),
                "type": generator.String('(Public University|Private University)'),
                "about": generator.String('abc[5-9]{4}\c[xyz]'),
                "location": generator.Name(),
                "logo": "https://source.unsplash.com/random/200x200",
            }
        )

        program_faker = Faker(
            cls=model.Program,
            init={
                "name": generator.Name(),
                "type": generator.String('(Undergraduate|Postgraduate)'),
                "about": generator.String('abc[5-9]{4}\c[xyz]')
            }
        )

        scholarship_faker = Faker(
            cls=model.Scholarship,
            init={
                "name": generator.Name(),
                "type": generator.String('(Undergraduate|Postgraduate)'),
                "about": generator.String('abc[5-9]{4}\c[xyz]')
            }
        )

        campus_faker = Faker(
            cls=model.Campus,
            init={
                "name": generator.Name(),
                "location": generator.String('abc[5-9]{4}\c[xyz]')
            }
        )

        facility_faker = Faker(
            cls=model.Facility,
            init={
                "name": generator.Name(),
                "image": "https://source.unsplash.com/random/50x50",
            }
        )

        contact_info_faker = Faker(
            cls=model.ContactInfo,
            init={
                "method": generator.String('(facebook|twitter|phone|instagram)'),
                "value": generator.String('abc[5-9]{4}\c[xyz]')
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

            print("Adding uni: %s" % uni)
            self.db.session.add(uni)
