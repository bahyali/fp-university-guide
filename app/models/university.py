from app import db
from datetime import datetime


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy

    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(255))
    location = db.Column(db.String(100))

    programs = db.relationship('Program', backref=db.backref('universities', lazy=True))
    scholarships = db.relationship('Scholarship', backref=db.backref('universities', lazy=True))
    campuses = db.relationship('Campus', backref=db.backref('universities', lazy=True))
    contact_info = db.relationship('ContactInfo', backref=db.backref('universities', lazy=True))

    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    about = db.Column(db.Text())
    tuition = db.relationship('Tuition', backref=db.backref('Program', lazy=True))

    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Scholarship(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    about = db.Column(db.Text)

    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Campus(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    facilities = db.relationship('Facility', backref=db.backref('Campus', lazy=True))

    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Facility(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    campus_id = db.Column(db.Integer, db.ForeignKey('campus.id'), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=False)

    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ContactInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)

    method = db.Column(db.String(100), nullable=False)
    value = db.Column(db.String(255), nullable=False)

    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
