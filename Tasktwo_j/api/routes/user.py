from routes.audio import app
from service.user import UserController
from db.models.user import User
from db.schemas.user import UserBase
from flask import request, jsonify
from uuid import uuid4
from db.session import db

# IVA
# 6f691f59-4943-4f4e-befb-ffec2b26f3e3
@app.route('/create_user', methods=['POST'])
def create_user():
    session = db.session()
    response = request.get_json()
    get_user = response['name']
    token = str(uuid4())
    if session.query(User.user).filter_by(user=get_user).first():
        return 'This user in DB'
    user_data = UserBase(name=get_user,
                         token=token)
    con_user = UserController()
    con_user.create_user(user_data)
    return 'Your token: {}'.format(token)

@app.route('/view_users', methods=['GET'])
def view_users():
    con_user = UserController()
    users = con_user.view_users()
    return jsonify(users)
