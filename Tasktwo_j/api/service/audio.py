from db.schemas.audio import AudioBase
from db.models.audio import Audio
from db.session import db

class AudioController:

    def audio_create(self, audio: AudioBase):
        with db.session() as session:
            data = Audio(audio=audio.audio_file,
                         token=audio.token)
            session.add(data)
            session.commit()
            session.refresh(data)
            return audio.audio_file

    def get_audio_file(self, index):
        with db.session() as session:
            audio = session.query(Audio).filter_by(id=index).first()
        return audio


