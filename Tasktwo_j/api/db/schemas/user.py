from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    token: str

class UserAudio(UserBase):
    audio_file: str