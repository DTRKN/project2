from db.session import db
from db.models.question import Questions
import requests

def api_get_data(api: str, num: int) -> dict:

    dict_data = {}
    prev = 'None'
    session = db.session()
    while num > len(dict_data):
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            for res in data:
                question_text = res['question']
                response_text = res['answer']

                if session.query(Questions.text_question).filter_by(text_question=question_text).first():
                    break
                dict_data[str(len(dict_data) + 1)] = {
                    'question': question_text,
                    'response': response_text,
                    'prev': prev
                }
                print(f'{len(dict_data)} Append question: {question_text}, response: {response_text}, prev: {prev}')
                prev = question_text
        else:
            raise ConnectionError(f'Error {response.status_code}. Check api url')
    return dict_data