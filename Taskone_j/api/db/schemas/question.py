from pydantic import BaseModel

class QuestionBase(BaseModel):
    question: str
    response: str
    prev: str
