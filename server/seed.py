from models import db, User, Puzzle, Message
from app import app, fetch_quote

NUM_PUZZLES = 1643
user1 = User(username = 'Yinsont', email = 'yinson.tso@gmail.com', password = 'yinnyt', score=750)
user2 = User(username = 'dfarlz97', email = 'dfarley1@binghamton.edu', password = 'Yuhyeet23!!', score=825)
user3 = User(username = 'BobbyB00ls', email = 'bb99@gmail.com', password = 'boolinbobby', score=900)
user4 = User(username = 'KuberneteAndSpaghetti12', email = 'ClusterClown.gmail.com', password = 'tenserflowin', score=50)
userInfo = [user1, user2, user3, user4]

message1 = Message(body='Wow! This game is almost as lit 🔥 as this UI', user=user1, score=user1.score)
message2 = Message(body=f'" Wisdom begins in wonder." Definetely going to remember that one', user=user2, score=user2.score)
message3 = Message(body='Tight.', user=user3, score=user3.score)
message4 = Message(body='This game is super fun and amazing. My only concern is whether or not this game be deployed via Kubernetes. By the way, have any of you fellow Lit-Crypters heard of Kubernetes? If not, WAKE UP.', user=user4, score=user4.score)
messageArr = [message1, message2, message3, message4]

def create_puzzles():
    puzzles = []

    for i in range(NUM_PUZZLES):
        quote = fetch_quote() 
        p = Puzzle(quote=quote)  
        db.session.add(p)
        puzzles.append(p)

    return puzzles

def seed_database():
    for user in userInfo:
        db.session.add(user)
    for message in messageArr:
        db.session.add(message)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        puzzles = create_puzzles()
        seed_database()