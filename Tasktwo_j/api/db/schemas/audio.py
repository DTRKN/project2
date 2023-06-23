from pydantic import BaseModel

class AudioBase(BaseModel):
    audio_file: str
    token: str

