import random
from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, User, Puzzle, Puzzlescore

fake = Faker()

# num = random.randint(0,1000)

def create_users():
    users = []
    usernames = []
    for _ in range(150):
        user = fake.name()
        while user in usernames:
            user = fake.name()
        usernames.append(user)

        u = User(
            user=user,
        )
        users.append(u)

    return users

def create_puzzles():
    puzzles = []
    ids = set()
    while len(puzzles) < 150:
        num = random.randint(0, 150)
        if num not in ids:
            ids.add(num)
            p = Puzzle(
                id=num,
            )
            puzzles.append(p)

    return puzzles


def create_puzzlescores(puzzles, users):
    puzzlescores = []
    for _ in range(50):
        num = random.randint(0, 150)
        puzzle = rc(puzzles)
        while not puzzle:
            puzzle = rc(puzzles)
        user = rc(users)
        while not user:
            user = rc(users)
        print(f"score: {num}, puzzle_id: {puzzle.id}, user_id: {user.id}")
        p = Puzzlescore(
            score=num,
            puzzle_id=puzzle.id,
            user_id=user.id
        )
        puzzlescores.append(p)
    return puzzlescores

if __name__ == '__main__':

    with app.app_context():
        print("Clearing db...")
        Puzzle.query.delete()
        User.query.delete()
        Puzzlescore.query.delete()

        print("Seeding puzzles...")
        puzzles = create_puzzles()
        db.session.add_all(puzzles)
        db.session.commit()

        # create users
        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        # create puzzlescores
        print("Seeding puzzlescores...")
        puzzlescores = create_puzzlescores(puzzles, users)
        db.session.add_all(puzzlescores)
        db.session.commit()

        print("Done seeding!")