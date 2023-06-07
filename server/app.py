#!/usr/bin/env python3

import os
from datetime import datetime
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'instance/app.db')}")

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Puzzle, User, PuzzleScore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def home():
    return ''

class Users(Resource):
    def get(self):
        try:
            users = User.query.all()
            new_users = [user.to_dict(only=("id", "name", "email")) for user in users]
            return new_users, 200

        except Exception as e: 
            return {"error": f"Bad request: {str(e)}"}, 400
        
    def post(self):
        try: 
            new_user = User(
                name=request.json['name'],
                email=request.json['email']
            )
            new_user.set_password(request.json['password'])
            db.session.add(new_user)
            db.session.commit()
            
            return new_user.to_dict(only=("id", "name", "email")), 201
        except Exception as e: 
            return { "error": f"400: Validation error: {str(e)}"}, 400

api.add_resource(Users, "/users")

class UsersById(Resource):
    def get(self, id):
        try: 
            user = User.query.get(id).to_dict(only=("id", "name", "email", "puzzles"))
            return user, 200
        except: 
            return {"error": "404: User not found"}, 404

api.add_resource(UsersById, "/users/<int:id>")

class Puzzles(Resource):
    def get(self):
        try: 
            puzzles = [puzzle.to_dict() for puzzle in Puzzle.query.all()]
            return puzzles, 200
        except Exception as e:
            return {'error': f'Bad request: {str(e)}'}, 400
            
api.add_resource(Puzzles, "/puzzles")

class PuzzlesById(Resource):
    def patch(self, id):
        try:
            puzzle = Puzzle.query.get(id)
            
            if request.json['key']:
                setattr(puzzle, 'key', request.json['key'])
                
            db.session.add(puzzle)
            db.session.commit()
            
            return puzzle.to_dict(), 202
        except Exception as e:
            return {"error": f"400: Validation error: {str(e)}"}, 400

    # def delete(self, id):
    #     try:
    #         puzzle = Puzzle.query.get(id)
            
    #         db.session.delete(puzzle)
    #         db.session.commit()
            
    #         return {}, 204
    #     except: 
    #         return {"error": "404: Puzzle not found"}, 404
        
api.add_resource(PuzzlesById, "/puzzles/<int:id>")

if __name__ == '__main__':
    app.run(port=5555, debug=True)