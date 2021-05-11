from app import db
from datetime import datetime


class BlogItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy

    title = db.Column(db.String(100), nullable=False)
    excerpt = db.Column(db.String(255))
    content = db.Column(db.Text())
    image = db.Column(db.String(255))

    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
