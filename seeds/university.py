import random

from flask_seeder import Seeder

from factories.university import university_factory, program_factory, scholarship_factory, campus_factory, \
    facility_factory, contact_info_factory


class UniversitySeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):

        for uni in university_factory.create(5):
            for program in program_factory.create(random.randint(1, 5)):
                uni.programs.append(program)

            for scholarship in scholarship_factory.create(random.randint(1, 5)):
                uni.scholarships.append(scholarship)

            for campus in campus_factory.create(random.randint(1, 5)):
                for facility in facility_factory.create(random.randint(1, 5)):
                    campus.facilities.append(facility)
                uni.campuses.append(campus)

            for contact_info in contact_info_factory.create(random.randint(1, 5)):
                uni.contact_info.append(contact_info)

            print("Adding University: %s" % uni)
            self.db.session.add(uni)
