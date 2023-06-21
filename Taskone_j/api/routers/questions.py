from flask import request, jsonify
from api.api_data import api_get_data
from api.controllers.questions import QuestionsController
from api.db.session import app
@app.route('/', methods=['GET'])
def connect():
    return {"message": "Connect"}

@app.route('/questions', methods=['POST'])
def generate_questions():

    api_url = 'https://jservice.io/api/random?count=1'
    data = request.get_json()
    num = data['questions_num']

    lst = api_get_data(api_url, num)

    quest = QuestionsController()
    for i in lst:
        quest.create_question(i[0], i[1], i[2])

    return jsonify(lst)

@app.route('/get_questions', methods=['GET'])
def get_questions():

    quest = QuestionsController()
    quest.get_all_questions()

@app.route('/drop_db', methods=['GET'])
def drop_questions():

    quest = QuestionsController
    quest.drop_all_quesions()




