from api.db.base_class import Base
from sqlalchemy import Column, String, Integer

class Audio(Base):

    __tablename__ = 'audio'
    id = Column(Integer, primary_key=True)
    audio_file = Column(String)
    token = Column(String)
    status = Column(Integer, default=0)
