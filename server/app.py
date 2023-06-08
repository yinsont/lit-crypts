#!/usr/bin/env python3

import os
from datetime import datetime
from flask import Flask, request, abort
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse
from models import db, User, Puzzle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)

@app.route('/')
def home():
    return 'Welcome to the puzzle app!'

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
        new_user.set_password(args['password'])
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
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('key', type=str, required=True)
        args = parser.parse_args()

        new_puzzle = Puzzle(
            name=args['name'],
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

@app.errorhandler(404)
def resource_not_found(e):
    return {'message': 'Resource not found'}, 404

@app.errorhandler(400)
def bad_request(e):
    return {'message': 'Bad request'}, 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
