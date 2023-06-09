from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from sqlalchemy import MetaData 
from sqlalchemy.orm import validates 
from sqlalchemy.ext.associationproxy import association_proxy 

db = SQLAlchemy()

class User(SerializerMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    role = db.relationship('Role', backref='users') 

    puzzles = db.relationship('Puzzle', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

class Role(SerializerMixin, db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name 

class Puzzle(SerializerMixin, db.Model):
    __tablename__ = 'puzzles'

    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.String(30), nullable=False)
    key = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    scores = db.relationship('PuzzleScore', backref='puzzle', lazy=True)

    serialize_rules = ('-user.puzzles',) 

class PuzzleScore(SerializerMixin, db.Model):
    __tablename__ = 'puzzlescores'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    puzzle_id = db.Column(db.Integer, db.ForeignKey('puzzles.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    serialize_rules = ('-puzzle.scores', '-user.scores')

    def __repr__(self):
        return f'<PuzzleScore {self.id}>'
