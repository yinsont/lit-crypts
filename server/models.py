from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()

# Models go here!
#user 
#leaderboard
#score
#puzzle

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

class Leaderboard(db.Model, SerializerMixin):
    __tablename__ = "leaderboards"
    id = db.Column(db.Integer, primary_key = True)
    points = db.Column(db.Integer)

class Score(db.Model, SerializerMixin):
    __tablename__ = "scores"
    id = db.Column(db.Integer, primary_key = True)
    scores = db.Column(db.Integer)


class Puzzle(db.Model, SerializerMixin):
    __tablename__ = "puzzles"
    id = db.Column(db.Integer, primary_key = True)
    puzzle_id = db.Column(db.Integer)
