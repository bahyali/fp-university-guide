from flask_seeder import Seeder, Faker, generator

from app.models.user import User
from werkzeug.security import generate_password_hash


class UserSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=User,
            init={
                "first_name": generator.Name(),
                "last_name": generator.Name(),
                "email": generator.Email(),
                "password": generate_password_hash('1234567890', method='sha256'),
                "grade": generator.String('[abc]'),
            }
        )

        # Create 5 users
        for user in faker.create(5):
            print("Adding user: %s" % user)
            self.db.session.add(user)
