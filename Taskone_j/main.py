from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
from datetime import datetime
import logging
import os

db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')
db_host = os.environ.get('DB_HOST')

app = Flask(__name__)
app.config['DEBUG'] = True

@app.errorhandler(500)
def internal_server_error(e):
    return str(e), 500

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"
#app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:tarawater@localhost:5432/project2"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text_question = db.Column(db.String(255))
    text_response = db.Column(db.String(255))
    date = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/questions', methods=['POST'])

def generate_questions():

    db.Model.metadata.create_all(db.engine)
    data = request.get_json()
    num = data['questions']
    prev = []
    lst = []
    api = 'https://jservice.io/api/random?count=1'


    while num > len(lst):
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            for res in data:
                question_text = res['question']
                answer_text = res['answer']
                existing_question = Question.query.all()
                for data in existing_question:
                    if data.text_question == question_text:
                        break
                else:
                    lst.append({'text_question': question_text,
                                'text_response': answer_text,
                                'prev': prev})

                    prev = {'prev_question': lst[-1]['text_question'],
                            'prev_response': lst[-1]['text_response']}
        else:
            raise ConnectionError(f'Error {response.status_code}. Check api url')

    for data in lst:
        new_question = Question(text_question=data['text_question'],
                                text_response=data['text_response'])
        db.session.add(new_question)
        db.session.commit()
    db.session.close()

    return jsonify(lst)

@app.route('/del_data', methods=['POST'])
def db_drop():
    db.drop_all()
    try:
        return 'Drop db accept'
    except:
        raise Exception('Error db')

@app.route('/data', methods=['GET'])
def db_questions():
    lst = []
    prev = []

    s = db.session
    questions = s.query(Question)

    try:
        for question in questions:
            lst.append({'id': question.id,
                        'text_question': question.text_question,
                        'text_response': question.text_response,
                        'date': question.date,
                        'prev': prev})
            prev = {'prev_question': lst[-1]['text_question'],
                    'prev_id': lst[-1]['id']}
    except:
        return 'DB no data inside'

    return jsonify(lst)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=5000)