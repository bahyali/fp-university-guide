from app.models.university import University
from app.models.blog import BlogItem
from app.models.news import NewsItem


class UniversityController:
    @staticmethod
    def index():
        return {
            'universities': University.query.order_by(University.name.asc()).all(),
        }
