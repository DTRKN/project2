from db.base_class import Base
from sqlalchemy import Column, Integer, String

class Questions(Base):

    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    text_question = Column(String(255))
    text_response = Column(String(255))
    prev = Column(String(255))



