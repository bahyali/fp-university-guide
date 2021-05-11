from app.models.university import University


class HomeController:
    @staticmethod
    def index():
        return {
            'featured_universities': University.query.limit(4).all(),
            'featured_blog_posts': [],
            'latest_news_items': []
        }
