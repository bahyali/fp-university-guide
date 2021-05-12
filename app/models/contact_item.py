from app import db
from datetime import datetime


class ContactItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text(), nullable=False)

    created_date = db.Column(db.DateTime, default=datetime.utcnow)
