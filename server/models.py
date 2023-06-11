from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import text

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    puzzlescores = db.relationship('Puzzlescore', backref='user', lazy=True)

    serialize_rules = ("-puzzlescores.user", "-puzzlescores.puzzle")

    def __repr__(self):
        return '<User %r>' % self.username

class Puzzle(db.Model, SerializerMixin): 
    __tablename__ = 'puzzles'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)

    scores = db.relationship('Puzzlescore', backref='puzzle', lazy=True)  

    serialize_rules = ("-scores.user", "-scores.puzzle")

    def __repr__(self):
        return '<Puzzle %r>' % self.id

class Puzzlescore(db.Model, SerializerMixin):
    __tablename__ = 'puzzlescores'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    puzzle_id = db.Column(db.Integer, db.ForeignKey('puzzles.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)

    serialize_rules = ("-user.puzzlescores", "-puzzle.scores")

    def __repr__(self):
        return '<Puzzlescore %r>' % self.id

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    username = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)

    def __repr__(self):
        return '<Message %r>' % self.body
