from db.schemas.user import UserBase
from db.models.user import User
from db.session import db

class UserController:

    def create_user(self, user: UserBase):
        with db.session() as session:
            data = User(user=user.name,
                        token=user.token)
            session.add(data)
            session.commit()
            session.refresh(data)

    def get_user_id(self, index):
        with db.session() as session:
            try:
                session.query(User).filter_by(id=index).first()
            except:
                return 'User is none'

    def view_users(self):
        with db.session() as session:
            try:
                users = session.query(User).all()
            except ConnectionError:
                return 'Not users in DB'

            result = []
            for get_user in users:
                result.append({'id': get_user.id,
                               'user': get_user.user,
                               'token': get_user.token})
            return result