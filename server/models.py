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
    score = db.Column(db.Integer)  

    def __repr__(self):
        return '<User %r>' % self.username

class Puzzle(db.Model, SerializerMixin): 
    __tablename__ = 'puzzles'

    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(255))  
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)  

    def __repr__(self):
        return '<Puzzle %r>' % self.id

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('messages', lazy=True))
    score = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)

    serialize_rules = ("-user.messages", "-user.id")
    def __repr__(self):
        return '<Message %r>' % self.body