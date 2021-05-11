from app.models.university import University
from app.models.blog import BlogItem
from app.models.news import NewsItem


class HomeController:
    @staticmethod
    def index():
        return {
            'featured_universities': University.query.order_by(University.created_date.desc()).limit(4).all(),
            'featured_blog_posts': BlogItem.query.order_by(BlogItem.created_date.desc()).limit(4).all(),
            'latest_news_items': NewsItem.query.order_by(NewsItem.created_date.desc()).limit(4).all()
        }
