from pydantic import BaseModel

class AudioBase(BaseModel):
    audio_file: str
    token: str

class AudioMp3(AudioBase):
    audio_file_mp3: str
