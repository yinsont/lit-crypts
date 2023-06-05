#!/usr/bin/env python3

# Standard library imports

# Remote library imports
# from flask import request
# from flask_restful import Resource

# Local imports
from config import app, db, api
from models import User, Recipe
import ipdb

# Views go here!
randomList = ["Tomatoes fall down the dragon wall", "Poorly wired circuit", "The same point of view", "Im that cat by the bar toasting to the good life", "Kill your friends guilt free."]
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
            "S", "T", "U", "V", "W", "X", "Y", "Z", "SPACE"]


def consoleTest():
    randomAlphabetCode()


def randomAlphabetCode(alphabet = alphabet):
    import random
    alphabetCopy = alphabet
    theCode = {}

    for letter in alphabetCopy:
        randomNumber2 = random.randint(0, len(randomizer) - 1)
        # print(f"{letter}: {randomizer[randomNumber2]}") uncomment this to see difference
        while randomizer[randomNumber2] in theCode.values():
            randomNumber2 = random.randint(0, len(randomizer) - 1)
                
        theCode[letter] = randomizer[randomNumber2]
        
    for key, value in theCode.items():
        print(f"{key} : {value}")
    return "Tomatoes"

ipdb.set_trace()
# if __name__ == '__main__':
#     app.run(port=5555, debug=True)


