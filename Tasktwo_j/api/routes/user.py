from api.db.session import app
from api.service.user import UserController
from api.db.models.user import User
from api.db.schemas.user import UserBase
from flask import request
from uuid import uuid4

@app.route('/create_user', methods=['POST'])
def create_user():
    response = request.get_json()
    user = response['name']
    token = str(uuid4())
    if not User.query(user).filter_by(user=user):
        user_data = UserBase(name=user,
                             token=token)
        con_user = UserController()
        con_user.create_user(user_data)
        return ' Your token: {}'.format(token)


