from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.utilities.exceptions import ValidationException


class SignupController:
    user_data = {}

    def __init__(self, user_data):
        self.user_data = user_data
        pass

    def register(self):
        self.validate()

        user: User = User(password=generate_password_hash(self.user_data['password'], method='sha256'),
                          email=self.user_data['email'],
                          grade=self.user_data['grade'],
                          first_name=self.user_data['first_name'],
                          last_name=self.user_data['last_name'])
        # add the new user to the database
        db.session.add(user)
        db.session.commit()

        return user

    def validate(self):
        user = User.query.filter_by(email=self.user_data['email']).first()
        if user:
            raise ValidationException('You are already registered, do you want to login?')
        pass


class LoginController:
    credentials = {}

    def __init__(self, credentials):
        self.credentials = credentials
        pass

    def check_credentials(self):
        email = self.credentials.get('email')
        password = self.credentials.get('password')

        user = User.query.filter_by(email=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            raise ValidationException('Please check your login details and try again')
        pass

        return user

