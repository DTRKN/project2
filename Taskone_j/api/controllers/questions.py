from db.models.question import Questions
from db.schemas.question import QuestionBase
from db.session import db


class QuestionsController:

    def create_question(self, quest: QuestionBase):
        with db.session() as session:

            question_obj = Questions(text_question=quest.question,
                                     text_response=quest.response,
                                     prev=quest.prev)
            session.add(question_obj)
            session.commit()
            session.refresh(question_obj)

    def get_all_questions(self):
        with db.session() as session:
            try:
                question = session.query(Questions).all()
            except ConnectionError:
                return "Not data in DB"

        return question

    def drop_all_quesions(self):
        db.drop_all()

        try:
            return 'Accept DB drop'
        except:
            raise Exception('Error db')