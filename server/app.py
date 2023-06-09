from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import openai
import gradio as gr

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Puzzle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    puzzle = db.Column(db.String(120), unique=True, nullable=False)
    solution = db.Column(db.String(120), unique=True, nullable=False)

class PuzzleScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    puzzle_id = db.Column(db.Integer, db.ForeignKey('puzzle.id'), nullable=False)

client = openai.Client()

def transcribe(audio):
    response = client.generate(
        prompt="Transcribe the following audio:",
        audio=audio,
        temperature=0.9,
        top_p=0.9,
        n=1,
        do_sample=True,
    )
    return response['choices'][0]['text']

@app.route('/submit_solution', methods=['POST'])
def submit_solution():
    audio_file = request.files['audio_file']
    filepath = audio_file.filename

    puzzle = Puzzle.query.get(request.form.get('puzzle_id'))
    solution_from_audio = transcribe(filepath)

    if puzzle.solution == solution_from_audio:
        # This assumes the User and Puzzle already exist
        score = PuzzleScore.query.filter_by(user_id=request.form.get('user_id'), puzzle_id=puzzle.id).first()
        if score is None:
            score = PuzzleScore(score=0, user_id=request.form.get('user_id'), puzzle_id=puzzle.id)
        score.score += 1
        db.session.add(score)
        db.session.commit()
        return jsonify({"message": "Correct solution", "score": score.score}), 200
    else:
        return jsonify({"message": "Wrong solution"}), 400

if __name__ == "__main__":
    db.create_all()
    gr.Interface(
        fn=transcribe,
        inputs=[
            gr.inputs.Audio(source="microphone", type='filepath')
        ],
        outputs=[
            'textbox'
        ],
        live=True
    ).launch()
