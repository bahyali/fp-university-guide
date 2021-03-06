import random

from flask_seeder import Seeder

from factories.university import university_factory, program_factory, scholarship_factory, campus_factory, \
    facility_factory, contact_info_factory


class UniversitySeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):

        for uni in university_factory.create(5):
            self.add_program(uni)

            self.add_scholarship(uni)

            self.add_campus(uni)

            self.add_contact_info(uni)

            print("Adding University: %s" % uni)

            self.db.session.add(uni)

    def add_contact_info(self, uni):
        for contact_info in contact_info_factory.create(random.randint(1, 5)):
            uni.contact_info.append(contact_info)

    def add_campus(self, uni):
        for campus in campus_factory.create(random.randint(1, 5)):
            self.add_facility(campus)
            uni.campuses.append(campus)

    def add_facility(self, campus):
        for facility in facility_factory.create(random.randint(1, 5)):
            campus.facilities.append(facility)

    def add_scholarship(self, uni):
        for scholarship in scholarship_factory.create(random.randint(1, 5)):
            uni.scholarships.append(scholarship)

    def add_program(self, uni):
        for program in program_factory.create(random.randint(1, 5)):
            uni.programs.append(program)
