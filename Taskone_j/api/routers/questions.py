from flask import request, jsonify
from controllers.api_data import api_get_data
from db.schemas.question import QuestionBase
from controllers.questions import QuestionsController
from db.session import app, engine
from db.base_class import Base

@app.route('/', methods=['GET'])
def connect():
    return {"message": "Connect"}
@app.route('/questions', methods=['POST'])
def generate_questions():

    Base.metadata.create_all(engine)

    api_url = 'https://jservice.io/api/random?count=1'
    data = request.get_json()
    num = data['questions_num']

    data_api = api_get_data(api_url, num)
    quest = QuestionsController()
    for i in range(1, num+1):
        quest_base = QuestionBase(question=data_api[str(i)]['question'],
                                  response=data_api[str(i)]['response'],
                                  prev=data_api[str(i)]['prev'])
        quest.create_question(quest_base)

    return jsonify(data_api)

@app.route('/get_questions', methods=['GET'])
def get_questions():

    quest = QuestionsController()
    questions = quest.get_all_questions()
    return jsonify(questions)


@app.route('/drop_db', methods=['GET'])
def drop_questions():

    quest = QuestionsController()
    result = quest.drop_all_quesions()
    return jsonify(result)




