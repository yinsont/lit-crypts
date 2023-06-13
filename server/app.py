from flask import Flask, make_response, jsonify, request, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
import requests
from flask_cors import CORS, cross_origin
from random import choice
import ipdb


from models import db, User, Puzzle, Message

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

# Function to fetch a quote
def fetch_quote():
    url = 'https://type.fit/api/quotes'
    r = requests.get(url=url)
    response = r.json()

    # Shuffle through quotes until a short enough one is found
    while True:
        quote = choice(response)
        if len(quote['text']) < 30:
            return quote['text']

class Users(Resource):
    def get(self):
        users = [u.to_dict(
            only=("id", "user")) for u in User.query.all()]
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
            puzzles = [p.to_dict(only=("id", "quote")) for p in Puzzle.query.all()]
            return puzzles, 200
        except:
            raise Exception({"error": "Something went wrong"})

    def post(self):
        try:
            new_puzzle = Puzzle(
                quote=fetch_quote(),  # Add a quote when creating a puzzle
            )
            db.session.add(new_puzzle)
            db.session.commit()
            return new_puzzle.to_dict(only=("id", "quote")), 201
        except:
            return {"error": "400: Validation error"}, 400

api.add_resource(Puzzles, "/puzzles")

class Login(Resource):
    def post(self):
        email = request.get_json()['email']
        password = request.get_json()['password']

        user = User.query.filter(User.email == email).first() 

        if user.authenticate(password):
            session['user_id'] = user.id 
            return user.to_dict(), 200
        
        return {'error': '401 Unauthorized'}, 401
    
api.add_resource(Login, '/login') 

class Signup(Resource):
    def post(self):
        email = request.get_json()['email'] 
        password = request.get_json()['password'] 
        admin = request.get_json()['admin']

        if email and password:
            new_user = User(email=email) 
            new_user.password_hash = password 
            new_user.admin = admin 
            db.session.add(new_user) 
            db.session.commit() 

            session['user_id'] = new_user.id 

            return new_user.to_dict(), 201 
        
        return {'error': '422 Unprocessable Entity'}, 422
    
api.add_resource(Signup, '/signup')

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first() 
        if user:
            return user.to_dict() 
        else:
            return {'message': '401: Not Authorized'}, 401
        
api.add_resource(CheckSession, '/check_session') 

class Logout(Resource):
    def delete(self):
        session['user_id'] = None 
        return {'message': '204: No Content'}, 204
    
api.add_resource(Logout, '/logout')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'GET':
        messages = Message.query.order_by('created_at').all()
        response = make_response(jsonify([message.to_dict() for message in messages]), 200)
    elif request.method == 'POST':
        data = request.get_json()
        message = Message(body=data['body'], user_id=data['user_id'])
        db.session.add(message)
        db.session.commit()
        response = make_response(jsonify(message.to_dict()), 201)
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
        response = make_response(jsonify(message.to_dict()), 200)
    elif request.method == 'DELETE':
        db.session.delete(message)
        db.session.commit()
        response = make_response(jsonify({'deleted': True}), 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
