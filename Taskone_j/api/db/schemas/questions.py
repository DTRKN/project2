from pydantic import BaseModel
import datetime

class QuestionSchema(BaseModel):
    id: int
    text_question: str
    text_response: str
    data: datetime

class Question_get(QuestionSchema):
    prev: str


