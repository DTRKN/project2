from pydantic import BaseModel

class Audio(BaseModel):
    audio_file: str
    token: str