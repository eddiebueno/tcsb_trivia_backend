from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Question

app = Flask(__name__)
setup_db(app)

CORS(app)


@app.route('/')
def index():
    return "Hello there"


@app.route('/api/questions')
def get_questions():
    questions = Question.query.all()
    q_list = [q.format() for q in questions]

    return jsonify(q_list)


@app.route('/api/questions', methods=['POST'])
def add_question():
    form_data = request.json
    try:
        new_question = Question(
            question=form_data["text"],
            answers=form_data["answers"],
            correct=form_data["correct"]
        )
        new_question.insert()
    except:
        return "Something went wrong"

    return jsonify({
        "success": True,
        "id": new_question.id
    })


if __name__ == "__main__":
    app.run()
