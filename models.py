from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.dialects.postgresql import ARRAY
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "trivia"
database_username = "postgres"
database_password = ""

database_path = "postgresql://{}/{}".format(
    database_username + ":" + database_password + "@localhost:5432",
    database_name
)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Question(db.Model):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answers = Column(ARRAY(String))
    correct = Column(Integer)

    def __init__(self, question, answers, correct):
        self.question = question
        self.answers = answers
        self.correct = correct

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'text': self.question,
            'answers': self.answers,
            'correct': self.correct
        }
