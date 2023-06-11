from models import db, User, Puzzle, Puzzlescore, Message
from app import app, fetch_quote
from faker import Faker

fake = Faker()

NUM_USERS = 10
NUM_PUZZLES = 10
NUM_SCORES = 10
NUM_MESSAGES = 10

def create_users():
    users = []

    for i in range(NUM_USERS):
        u = User(
            username=f'user{i}',
            email=f'user{i}@example.com',
            password=f'password{i}'
        )
        db.session.add(u)
        users.append(u)

    return users

def create_puzzles():
    puzzles = []

    for i in range(NUM_PUZZLES):
        quote = fetch_quote()  # Fetch a short quote
        p = Puzzle(quote=quote)  # Add quote to the puzzle
        db.session.add(p)
        puzzles.append(p)

    return puzzles

def create_scores(users, puzzles):
    scores = []

    for i in range(NUM_SCORES):
        ps = Puzzlescore(
            score=i,
            user_id=users[i % NUM_USERS].id,
            puzzle_id=puzzles[i % NUM_PUZZLES].id
        )
        db.session.add(ps)
        scores.append(ps)

    return scores


def create_messages(users):
    messages = []

    for i in range(NUM_MESSAGES):
        m = Message(
            body=f'{fake.sentence(nb_words=5)}',
            username=users[i % NUM_USERS].username
        )
        db.session.add(m)
        messages.append(m)

    return messages

def seed_database():
    print("Seeding users...")
    users = create_users()

    print("Seeding puzzles...")
    puzzles = create_puzzles()

    print("Seeding scores...")
    scores = create_scores(users, puzzles)

    print("Seeding messages...")
    messages = create_messages(users)

    print("Committing changes to database...")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_database()
