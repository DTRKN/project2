from db.schemas.audio import AudioBase
from db.models.audio import Audio
from db.session import db

class AudioController:

    def audio_create(self, audio: AudioBase):
        with db.session() as session:
            data = Audio(audio_file=audio.audio_file,
                         token=audio.token)
            audio_copy = session.query(Audio.id).filter_by(audio_file=audio.audio_file).first()
            if not audio_copy:
                session.add(data)
                session.commit()
                session.refresh(data)
                return session.query(Audio.id).filter_by(audio_file=audio.audio_file).first()
            return audio_copy

    def get_audio_file_id(self, index):
        with db.session() as session:
            audio = session.query(Audio.audio_file).filter_by(id=index).first()
        return audio

    def view_audio(self):
        with db.session() as session:
            try:
                audio = session.query(Audio).all()
            except ConnectionError:
                return 'Not users in DB'

            result = []
            for get_audio in audio:
                result.append({'id': get_audio.id,
                               'audio_file': get_audio.audio_file,
                               'token': get_audio.token})
            return result



