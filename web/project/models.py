from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), unique=False, nullable=True)
    last_name = db.Column(db.String(128), default=False, nullable=True)
    email = db.Column(db.String(128), unique=True, nullable=True)
    phone_number = db.Column(db.String(128), unique=True, nullable=True)

    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number
        }
