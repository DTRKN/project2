from typing import List
from api.db.models.question import Questions
import requests
def api_get_data(api: str, num: int) -> List[List[str, str, str]]:

    lst = []
    prev = []
    while num > len(lst):
        response = requests.get(api)  # ...?
        if response.status_code == 200:
            data = response.json()
            for res in data:
                question_text = res['question']
                response_text = res['answer']

                if Questions.query.filter_by(text_question=question_text):
                    break
                lst.append([question_text, response_text, prev])
                print(f'Append question: {question_text}, response: {response_text}, prev: {prev}')
                prev = question_text
        else:
            raise ConnectionError(f'Error {response.status_code}. Check api url')
    return lst