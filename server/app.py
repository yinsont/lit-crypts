# from flask import Flask, request, jsonify, make_response, Resource
# import requests
# from flask_cors import CORS
# from flask_restful import Api, Resource
# from models import db, User, Puzzle, Puzzlescore, Message
# from flask_migrate import Migrate

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
import requests
from flask_cors import CORS
from random import choice

from models import db, User, Puzzle, Puzzlescore, Message
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

class Users(Resource):

    def get(self):
        users = [u.to_dict(
            only=("id", "user", "puzzlescores")) for u in User.query.all()]

        return users, 200

    def post(self):
        try:
            new_user = User(
                user=request.json['user'],
            )

            db.session.add(new_user)
            db.session.commit()

            return new_user.to_dict(only=("id", "user")), 201
        except:
            return {"error": "400: Validation error"}, 400


api.add_resource(Users, "/users")


class Puzzles(Resource):

    def get(self):
        try:

            puzzles = [p.to_dict(only=("id")) for p in Puzzle.query.all()]

            return puzzles, 200

        except:
            raise Exception({"error": "Something went wrong"})


api.add_resource(Puzzles, "/puzzles")


class Puzzlescores(Resource):

    def post(self):
        try:
            new_puzzlescore = Puzzlescore(
                id = request.json['id'],
                user_id=request.json['user_id'],
                puzzle_id=request.json['puzzle_id']
            )

            db.session.add(new_puzzlescore)
            db.session.commit()

            
            return new_puzzlescore.puzzle.to_dict(only=("id", "score")), 201

        except:
            return {
                "error": "400: Validation error"
            }, 400


api.add_resource(Puzzlescores, "/puzzlescores")

from random import choice

@app.route('/quote')
def fetch_quote():
    url = 'https://type.fit/api/quotes'
    r = requests.get(url=url)
    response = r.json()

    # Shuffle through quotes until a short enough one is found
    while True:
        quote = choice(response)
        if len(quote['text']) < 30:
            return jsonify(quote)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'GET':
        messages = Message.query.order_by('created_at').all()

        response = make_response(
            jsonify([message.to_dict() for message in messages]),
            200,
        )
    
    elif request.method == 'POST':
        data = request.get_json()
        message = Message(
            body=data['body'],
            username=data['username']
        )

        db.session.add(message)
        db.session.commit()

        response = make_response(
            jsonify(message.to_dict()),
            201,
        )

    return response

@app.route('/messages/<int:id>', methods=['PATCH', 'DELETE'])
def messages_by_id(id):
    message = Message.query.filter_by(id=id).first()

    if request.method == 'PATCH':
        data = request.get_json()
        for attr in data:
            setattr(message, attr, data[attr])
            
        db.session.add(message)
        db.session.commit()

        response = make_response(
            jsonify(message.to_dict()),
            200,
        )

    elif request.method == 'DELETE':
        db.session.delete(message)
        db.session.commit()

        response = make_response(
            jsonify({'deleted': True}),
            200,
        )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)