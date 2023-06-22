from api.db.schemas.audio import AudioBase
from api.db.models.audio import Audio
from api.db.session import db

class AudioController:

    def audio_create(self, audio: AudioBase):
        with db.session as session:
            data = Audio(audio=audio.audio_file,
                         token=audio.token)
            session.add(data)
            session.commit()
            session.refresh()

    def converting_audio(self):
        pass
        # audio.wav --> audio.mp3

    def unloading_audio_file(self):
        with db.session as session:
            data = session.query(Audio).all()
        return data
