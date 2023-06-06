#!/usr/bin/env python3

# Standard library imports

# Remote library imports

# Local imports

from models import db
# from models import User, Recipe
from flask import Flask, session, abort, redirect, request
from flask_migrate import Migrate
from flask_restful import Api, Resource


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

import ipdb
# Views go here!
randomList = ["Rolling eyes fall down the dragon wall", "Poorly wired circuit", "", "Im that cat by the bar toasting to the good life", "Kill your friends guilt free"]
randomizer = ["😂", "🗿", "💀", "🙄", "🤑", "👨🏿‍🌾", 
              "🤵🏻", "🐸", "🦍", "🔫", "🤩", "🥶", 
              "🍕", "🧠", "🐱‍🏍", "💃🏻", "👨‍👩‍👧‍👦", "🎅", 
              "👃", "👮🏻‍♂️", "⚡", "🏃🏿‍♂️", "👩🏻‍🎤", "🌟", 
              "🤳", "🎱", "🎈", "👑", "🌊", "🥏", 
              "🎮", "💎", "🎩", "🔪", "🎁", "🥩",
              "🧊", "🍆", "🧀", "🍩", "🚔", "🌕",
              "🔥", "🌚", "⚓", "🗼", "✈", "☁",
              "👧", "🌠", "🌋", "🌌", "🛐", "🅱",
              "A", "B", "C", "D", "E", "F",
              "G", "H", "I","J", "K", "L", 
              "M", "N", "O", "P", "Q","R",
              "S", "T", "U", "V", "W", "X", 
              "Y", "Z", "1", "2", "3", "4",
              "5", "6", "7", "8", "9", "0",
              "!", "@", "#", "$", "%", "^",
              "&", "*", "(", ")", "-", "+",
              "<", ">", "/", "|", "💨", "💢"]

alphabet = ["A", "B", "C", "D", "E", "F","G", "H", "I",
            "J", "K", "L", "M", "N", "O", "P", "Q","R",
            "S", "T", "U", "V", "W", "X", "Y", "Z"]

theCode = {}

def consoleTest():
    randomAlphabetCode()
    makeTheMessage()

def makeTheMessage():
    import random
    randomNumber = random.randint(0, len(randomList) - 1)
    message = randomList[randomNumber]
    messageCopy = message
    cryptedMessage = ""
    for letter in messageCopy:
        if letter == ' ':
            cryptedMessage += letter
        elif letter == "'":
            cryptedMessage += letter
        else:
            print(f"{letter} : {theCode[letter.upper()]}")
            cryptedMessage += theCode[letter.upper()]
    #     cryptedMessage.replace(letter, theCode[f"{letter.upper()}"])
    
    print(f"CRYPTED: {cryptedMessage} ")

def randomAlphabetCode(alphabet = alphabet):
    alphabetCopy = alphabet

    for letter in alphabetCopy:
        import random
        randomNumber2 = random.randint(0, len(randomizer) - 1)
        # print(f"{letter}: {randomizer[randomNumber2]}") uncomment this to see difference
        while randomizer[randomNumber2] in theCode.values():
            randomNumber2 = random.randint(0, len(randomizer) - 1)
                
        theCode[letter] = randomizer[randomNumber2]
        
    # for key, value in theCode.items():        check the encryption
    #     print(f"{key} : {value}")
    return "Tomatoes" #this return statement is literally serving 0 purpose


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)


