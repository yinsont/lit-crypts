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
    created_at = db.Column(db.DateTime, default=db.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=db.datetime.utcnow)
    last_login = db.Column(db.DateTime)
    role = db.Column(db.String(32), default='user') # Added user role

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

class Role(db.Model, SerializerMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')


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

    serialize_rules = ('-users.puzzle') 

class PuzzleScore(SerializerMixin, db.Model):
    __tablename__ = 'puzzlescores'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    puzzle_id = db.Column(db.Integer, db.ForeignKey('puzzles.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    serialize_rules = ('-puzzle.puzzlescores', '-user.puzzlescores')

    
    def __repr__(self):
        return f'<PuzzleScore {self.id}>'

""" 
#!/usr/bin/env python3

import os
from datetime import datetime
from flask import Flask, request, abort
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from models import db, User, PuzzleScore, Puzzle, Role

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app) 

api = Api(app)

@app.route('/') 
def home():
    return ''

class User(SerializerMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=db.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=db.datetime.utcnow)
    last_login = db.Column(db.DateTime)
    role = db.Column(db.String(32), default='user') # Added user role

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

class Role(db.Model, SerializerMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

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

    serialize_rules = ('-users.puzzle') 

class PuzzleScore(SerializerMixin, db.Model):
    __tablename__ = 'puzzlescores'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    puzzle_id = db.Column(db.Integer, db.ForeignKey('puzzles.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    serialize_rules = ('-puzzle.puzzlescores', '-user.puzzlescores')

    @validates('score')
    def validate_score(self, key, score): # Modified the argument from time to score
        if not 0 <= score <= 1000:
            raise ValueError("Score must be within limits")
        return score
    
    def __repr__(self):
        return f'<PuzzleScore {self.id}>'

# Below is the original code for the Flask application.

@app.route('/')
def home():
    return ''

class Users(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        new_user = User(
            name=args['name'],
            email=args['email']
        )
        new_user.password = args['password'] # Changed from set_password to password due to the change in the User model
        db.session.add(new_user)
        db.session.commit()

        return new_user.to_dict(only=("id", "name", "email")), 201

api.add_resource(Users, "/users")

class UserById(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user.to_dict(), 200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {}, 204

    def patch(self, user_id):
        user = User.query.get_or_404(user_id)
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        args = parser.parse_args()

        if args['name'] is not None:
            user.name = args['name']
        if args['email'] is not None:
            user.email = args['email']
        db.session.commit()

        return user.to_dict(), 200

api.add_resource(UserById, "/users/<int:user_id>")

class Puzzles(Resource):
    def get(self):
        puzzles = Puzzle.query.all()
        return [puzzle.to_dict() for puzzle in puzzles], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sentence', type=str, required=True) # Changed from name to sentence to match the Puzzle model
        parser.add_argument('key', type=str, required=True)
        args = parser.parse_args()

        new_puzzle = Puzzle(
            sentence=args['sentence'], # Changed from name to sentence to match the Puzzle model
            key=args['key']
        )
        db.session.add(new_puzzle)
        db.session.commit()

        return new_puzzle.to_dict(), 201

api.add_resource(Puzzles, "/puzzles")

class PuzzleById(Resource):
    def get(self, puzzle_id):
        puzzle = Puzzle.query.get_or_404(puzzle_id)
        return puzzle.to_dict(), 200

    def patch(self, puzzle_id):
        puzzle = Puzzle.query.get_or_404(puzzle_id)
        parser = reqparse.RequestParser()
        parser.add_argument('key', type=str)
        args = parser.parse_args()

        if args['key'] is not None:
            puzzle.key = args['key']
        db.session.commit()

        return puzzle.to_dict(), 200

    def delete(self, puzzle_id):
        puzzle = Puzzle.query.get_or_404(puzzle_id)
        db.session.delete(puzzle)
        db.session.commit()
        return {}, 204

api.add_resource(PuzzleById, "/puzzles/<int:puzzle_id>")

class PuzzleScores(Resource):
    def get(self):
        scores = PuzzleScore.query.all()
        return [score.to_dict() for score in scores], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('score', type=int, required=True)
        parser.add_argument('puzzle_id', type=int, required=True)
        parser.add_argument('user_id', type=int, required=True)
        args = parser.parse_args()

        new_score = PuzzleScore(
            score=args['score'],
            puzzle_id=args['puzzle_id'],
            user_id=args['user_id']
        )
        db.session.add(new_score)
        db.session.commit()

        return new_score.to_dict(), 201

api.add_resource(PuzzleScores, "/puzzlescores")

class PuzzleScoreById(Resource):
    def get(self, score_id):
        score = PuzzleScore.query.get_or_404(score_id)
        return score.to_dict(), 200

    def patch(self, score_id):
        score = PuzzleScore.query.get_or_404(score_id)
        parser = reqparse.RequestParser()
        parser.add_argument('score', type=int)
        args = parser.parse_args()

        if args['score'] is not None:
            score.score = args['score']
        db.session.commit()

        return score.to_dict(), 200

    def delete(self, score_id):
        score = PuzzleScore.query.get_or_404(score_id)
        db.session.delete(score)
        db.session.commit()
        return {}, 204

api.add_resource(PuzzleScoreById, "/puzzlescores/<int:score_id>")

@app.errorhandler(404)
def resource_not_found(e):
    return {'message': 'Resource not found'}, 404

@app.errorhandler(400)
def bad_request(e):
    return {'message': 'Bad request'}, 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)

"""

