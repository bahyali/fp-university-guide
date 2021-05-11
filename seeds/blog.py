from flask_seeder import Seeder, Faker
from faker import Faker as Generator
from app.models.blog import BlogItem

fake = Generator()


class BlogSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        fake_blog_items = Faker(
            cls=BlogItem,
            init={
                "title": lambda: '%s University' % fake.sentence(),
                "excerpt": lambda: fake.paragraph(),
                "content": lambda: fake.text(),
                "image": lambda: fake.image_url(),
            }
        )

        # Create 5 users
        for blog_item in fake_blog_items.create(5):
            print("Adding Blog Item: %s" % blog_item)
            self.db.session.add(blog_item)
