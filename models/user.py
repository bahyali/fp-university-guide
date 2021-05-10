from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy

    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))

    grade = db.Column(db.String(1000))

    created_date = db.Column(db.DateTime, default=db.datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=db.datetime.now, onupdate=db.datetime.now)
