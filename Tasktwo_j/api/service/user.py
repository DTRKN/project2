from api.db.schemas.user import UserBase, UserAudio
from api.db.models.user import User
from api.db.session import db

class UserController:

    def create_user(self, user: UserBase):
        with db.session as session:
            data = User(user=user.name,
                        token=user.token)
            session.add(data)
            session.commit()
            session.refresh()

    def append_audio_user(self, user: UserAudio):
        with db.session as session:
            data = User(audio_file=user.audio_file)
            session.add(data)
            session.commit()
            session.refresh()