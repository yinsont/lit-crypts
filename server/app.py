#!/usr/bin/env python3
import os
from datetime import datetime
from flask import Flask, request, abort, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse
from models import db, User, Puzzle, PuzzleScore
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def home():
    return ''

@app.route('/quote')
def fetch_quote():
    url = 'https://type.fit/api/quotes'
    params = {'key':'value'}
    r = requests.get(url = url, params = params) 
    response = r.json()
    return jsonify(response)

class Users(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200

    def post(self):

        new_user = User(
            name=request.json['name'],
            email=request.json['email']
        )
        new_user.set_password(request.json['password'])
        db.session.add(new_user)
        db.session.commit()

        return new_user.to_dict(only=("id", "name", "email")), 201

api.add_resource(Users, "/users")

class UserById(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return {"error": "404: User not found"}, 404
        return user.to_dict(), 200

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return {"error": "404: User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {}, 204

    def patch(self, user_id):
        user = User.query.filter_by(id=user_id).first()
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

        new_puzzle = Puzzle(
            name=request.json['name'],
            key=request.json['key']
        )
        db.session.add(new_puzzle)
        db.session.commit()

        return new_puzzle.to_dict(), 201

api.add_resource(Puzzles, "/puzzles")

class PuzzleById(Resource):
    def get(self, puzzle_id):
        puzzle = Puzzle.query.filter_by(id=puzzle_id).first()
        if puzzle is None:
            return {"error": "404: Puzzle not found"}, 404
        return puzzle.to_dict(), 200

    def patch(self, puzzle_id):
        puzzle = Puzzle.query.filter_by(id=puzzle_id).first()
        parser = reqparse.RequestParser()
        parser.add_argument('key', type=str)
        args = parser.parse_args()

        if args['key'] is not None:
            puzzle.key = args['key']
        db.session.commit()

        return puzzle.to_dict(), 200

    def delete(self, puzzle_id):
        puzzle = Puzzle.query.filter_by(id=puzzle_id).first()
        if puzzle is None:
            return {"error": "404: Puzzle not found"}, 404
        db.session.delete(puzzle)
        db.session.commit()
        return {}, 204

api.add_resource(PuzzleById, "/puzzles/<int:puzzle_id>")

class PuzzleScores(Resource):
    def get(self):
        scores = PuzzleScore.query.all()
        return [score.to_dict() for score in scores], 200

    def post(self):

        new_score = PuzzleScore(
            score=request.json['score'],
            puzzle_id=request.json['puzzle_id'],
            user_id=request.json['user_id']
        )
        db.session.add(new_score)
        db.session.commit()

        return new_score.to_dict(), 201

api.add_resource(PuzzleScores, "/puzzlescores")

class PuzzleScoreById(Resource):
    def get(self, score_id):
        score = PuzzleScore.query.filter_by(id=score_id).first()
        if score is None:
            return {"error": "404: Score not found"}, 404
        return score.to_dict(), 200

    def patch(self, score_id):
        score = PuzzleScore.query.filter_by(id=score_id).first()
        parser = reqparse.RequestParser()
        parser.add_argument('score', type=int)
        args = parser.parse_args()

        if args['score'] is not None:
            score.score = args['score']
        db.session.commit()

        return score.to_dict(), 200

    def delete(self, score_id):
        score = PuzzleScore.query.filter_by(id=score_id).first()
        if score is None:
            return {"error": "404: Score not found"}, 404
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
