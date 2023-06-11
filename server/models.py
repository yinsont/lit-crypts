from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, nullable=False)

    puzzlescores = db.relationship("Puzzlescore", backref='user')

    serialize_rules = ("-puzzles.user",)
    
    @validates('user')
    def validate_user(self, key, user):
        if not user and len(user) < 0:
            raise ValueError("User must be present.")

        return user

    def __repr__(self):
        return f'<User {self.id}: {self.user}>'
    
class Puzzle(db.Model,SerializerMixin): 
    __tablename__ = 'puzzles'

    id = db.Column(db.Integer, primary_key=True)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    def validate_id(self, key, id):
        if not id: 
            raise ValueError("ID must be unique.")

        return id
    
class Puzzlescore(db.Model, SerializerMixin):
    __tablename__ = 'puzzlescores'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    puzzle_id = db.Column(db.Integer, db.ForeignKey('puzzles.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ("-user.puzzlescores", "-puzzle.missions")
    
    @validates('user_id')
    def validate_user_id(self, key, user_id):
        if not user_id:
            raise ValueError("User must exist")

        return user_id

    @validates('puzzle_id')
    def validate_puzzle_id(self, key, puzzle_id):
        if not puzzle_id:
            raise ValueError("Puzzle must exist")

        return puzzle_id
    
class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    username = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Message by {self.username}: {self.body[:10]}...>'