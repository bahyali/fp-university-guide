from flask_seeder import Seeder, Faker
from faker import Faker as FakeGenerator
from app.utilities.seeding import FakerIntegration as Generator
from app.models.news import NewsItem

fake = FakeGenerator()


class NewsSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        fake_blog_items = Faker(
            cls=NewsItem,
            init={
                "title": Generator(lambda: fake.sentence()),
                "excerpt": Generator(lambda: fake.paragraph()),
                "content": Generator(lambda: fake.text()),
                "image": Generator(lambda: fake.image_url(500, 500).replace('lorempixel.com', 'loremflickr.com')),
            }
        )

        # Create 5 users
        for blog_item in fake_blog_items.create(5):
            print("Adding News Item: %s" % blog_item)
            self.db.session.add(blog_item)
