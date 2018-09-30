# Import SQLAlchemy
from app import db


class User(db.Model):
    """
    Create a User table
    """

    # Table will be named in plural
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    questions = db.relationship('Question', backref='user',
                                lazy='dynamic')

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Question(db.Model):
    """
    Create a Question table
    """

    # Table will be named in plural
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    answers = db.relationship('Answer', backref='question',
                              lazy='dynamic')

    def __repr__(self):
        return '<Question: {}>'.format(self.name)


class Answer(db.Model):
    """
    Create an Answer table
    """

    # Table will be named in plural
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    is_preferred_answer = db.Column(db.Boolean, default=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def __repr__(self):
        return '<Answer: {}>'.format(self.name)
