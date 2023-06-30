from db.base_class import Base
from sqlalchemy import Column, Integer, DateTime, String
import datetime
class Questions(Base):

    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    text_question = Column(String(255))
    text_response = Column(String(255))
    prev = Column(String(255))
    date = Column(DateTime, default=datetime)


