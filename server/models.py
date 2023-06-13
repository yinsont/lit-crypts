from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import text
from sqlalchemy.orm import validates 
from sqlalchemy.ext.hybrid import hybrid_property 
from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String)
    score = db.Column(db.Integer)  

    puzzle_scores = db.relationship('Puzzle_Score', backref='user')

    serialize_rules = ('-puzzle_scores.user',)

    @hybrid_property 
    def password_hash(self):
        raise Exception('Password hashes may not be viewed.') 
    
    @password_hash.setter 
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8')
        )
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8')
        )
    
    @validates('email') 
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('Failed email validation: Email must include a @') 
        return email 

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
    

class Puzzle_Score(db.Model, SerializerMixin):
    __tablename__ = 'puzzle_scores'
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())



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
