from api.db.base_class import Base
from sqlalchemy import Column, String, Integer

class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user = Column(String)
    token = Column(String)
    audio_file = Column(String)
