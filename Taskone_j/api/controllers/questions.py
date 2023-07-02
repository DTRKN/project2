from db.models.question import Questions
from db.schemas.question import QuestionBase
from db.session import db, engine
from db.base_class import Base


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
                questions_db = session.query(Questions).all()
            except ConnectionError:
                return "Not data in DB"

            result = []
            for question in questions_db:
                result.append({"id": question.id,
                                "question": question.text_question,
                                "response": question.text_response,
                                "prev": question.prev})
            return result

    def drop_all_quesions(self):
        try:
            Base.metadata.drop_all(engine)
            return 'All tables dropped successfully'
        except Exception as e:
            return f'An error occurred: {str(e)}'
