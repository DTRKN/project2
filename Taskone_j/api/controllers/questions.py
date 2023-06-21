from api.db.models.question import Questions
from api.db.schemas.questions import QuestionSchema
from api.db.session import db

class QuestionsController:

    def create_question(self, question, response, prev):
        with db.session as session:
            question_obj = Questions(text_question=question,
                                     text_response=response,
                                     prev=prev)

            session.add(question_obj)
            session.commit()
            session.refresh(question_obj)
    def get_all_questions(self):
        with db.session as session:
            question = session.query(Questions).all()
        return question

    def drop_all_quesions(self):
        db.drop_all()
        try:
            return 'Accept DB drop'
        except:
            raise Exception('Error db')