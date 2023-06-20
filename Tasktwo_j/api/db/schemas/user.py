from pydantic import BaseModel

class User(BaseModel):
    name: str
    token: str