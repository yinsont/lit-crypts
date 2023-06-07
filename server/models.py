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

# and models.py: from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from sqlalchemy.orm import validates
# from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

class Puzzle(db.Model, SerializerMixin):
    __tablename__ = 'puzzles'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String)
    date_released = db.Column(db.DateTime)
    original = db.Column(db.String)
    # partially_solved = db.Column(db.String) 

    puzzle_scores = db.relationship("PuzzleScore", back_populates= "puzzle", cascade="all,delete")

    serialize_only = ("id", "key", "original")

    def __repr__(self):
        return f'<Puzzle {self.id}: {self.id}>'

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)

    puzzle_scores = db.relationship("PuzzleScore", back_populates= "user.id")

    puzzles = association_proxy("puzzle_scores", "puzzle")

    serialize_rules = ("-puzzle_scores.user",)

    @validates('name')
    def validate_name(self, key, name):
        print('Inside the name validation')
        if not name or len(name) < 1: 
            raise ValueError("Name must exist")

        return name

    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}: {self.name}>'

class PuzzleScore(db.Model, SerializerMixin):
    __tablename__ = 'puzzle_scores'

    id = db.Column(db.Integer, primary_key=True)
    time_start = db.Column(db.DateTime)
    time_solved = db.Column(db.DateTime) 
    attempts = db.Column(db.Integer) 
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    puzzle_id = db.Column(db.Integer, db.ForeignKey("puzzles.id"))

    user = db.relationship('User', back_populates='puzzle_scores')
    puzzle = db.relationship('Puzzle', back_populates='puzzle_scores')

    serialize_rules = ("-user.puzzle_scores", "-puzzle.puzzle_scores")

    def __repr__(self):
        return f'<PuzzleScore {self.id}>'
