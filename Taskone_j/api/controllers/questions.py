from api.db.models.question import Questions
from api.db.schemas.question import QuestionBase
from api.db.session import db

class QuestionsController:

    def create_question(self, quest: QuestionBase):
        with db.session as session:
            question_obj = Questions(text_question=quest.question,
                                     text_response=quest.response,
                                     prev=quest.prev)
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