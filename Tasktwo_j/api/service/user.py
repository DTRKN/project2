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

    def get_user_id(self, id):
        with db.session as session:
            try:
                session.query(User).filter_by(id=id).first()
            except:
                return 'User is none'
