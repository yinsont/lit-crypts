from flask import Flask, request
from bardapi import Bard
import os

# Set the Bard API key in the environment variable

app = Flask(__name__)

bard = Bard()

@app.route('/')
def index():
    """Get a quote from Bard-API."""
    input_text = 'Provide a famous and historically accurate quote'
    bard_output = bard.get_answer(input_text)['content']
    return bard_output

@app.route('/business')
def business():
    """Get a quote about business from Bard-API."""
    input_text = 'Provide a famous and historically accurate quote about business'
    bard_output = bard.get_answer(input_text)['content']
    return bard_output

@app.route('/kubernetes')
def kubernetes():
    """Get a quote about Kubernetes from Bard-API."""
    input_text = 'Provide a famous and historically accurate quote about Kubernetes'
    bard_output = bard.get_answer(input_text)['content']
    return bard_output

@app.route('/art')
def art():
    """Get a quote about art from Bard-API."""
    input_text = 'Provide a famous and historically accurate quote about art'
    bard_output = bard.get_answer(input_text)['content']
    return bard_output

@app.route('/philosophy')
def philosophy():
    """Get a quote about philosophy from Bard-API."""
    input_text = 'Provide a famous and historically accurate quote about philosophy'
    bard_output = bard.get_answer(input_text)['content']
    return bard_output

@app.route('/literature')
def literature():
    """Get a quote about literature from Bard-API."""
    input_text = 'Provide a famous and historically accurate quote about literature'
    bard_output = bard.get_answer(input_text)['content']
    return bard_output

@app.route('/politics')
def politics():
    """Get a quote about politics from Bard-API."""
    input_text = 'Provide a famous and historically accurate quote about politics'
    bard_output = bard.get_answer(input_text)['content']
    return bard_output

@app.route('/popular-culture')
def popular_culture():
    """Get a quote about popular culture from Bard-API."""
    input_text = 'Provide a famous and historically accurate quote about popular culture'
    bard_output = bard.get_answer(input_text)['content']
    return bard_output

if __name__ == "__main__":
    app.run()
