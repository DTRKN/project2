
from flask import Flask, request, jsonify
from models import db, User, Audio
import uuid
import os
import logging

db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')
db_host = os.environ.get('DB_HOST')

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"
#app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:{os.getenv('DB_PASSWORD')}@localhost:5432/project2"
db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/user', methods=['POST'])
def create_user():

    with app.app_context():
        data = request.get_json()
        name = data['user']
        token = str(uuid.uuid4())
        users = [x.user for x in User.query.all()]
        if name not in users:

            new_user = User(user=name, token=token)
            db.session.add(new_user)
            db.session.commit()

            return ['Added new user {}'.format(name),
                    'Your token: {}'.format(token)]

        return 'Already exists user {}'.format(name)
@app.route('/audio', methods=['POST'])
def conversion_audio():
    with app.app_context():
        data = request.get_json()
        user = data['user']
        token_user = data['token']
        audio_file = data.get('audio_file')
        audio_name = audio_file.split('.')[0]
        audio_format = audio_file.split('.')[-1]
        token = str(uuid.uuid4())
        flag = False
        for data in User.query.all():
            if data.user == user and data.token == token_user:
                if audio_name not in [x.audio_file.split('.')[0] for x in Audio.query.all()]:
                    flag = True
        if flag:
            if audio_format == 'wav':
                audio = audio_name + '.mp3'
                new_audio = Audio(audio_file=audio, token=token)
                db.session.add(new_audio)
                db.session.commit()

                return jsonify([f'По этой ссылке вы можете скачать свой файл аудио в формате mp3',
                       f'http://example.com/record?id={token}&user={data.id}'])
            else:
                return 'Incorrect format. Format must equal .wav'
        else:
            return f'ConnectionError: User not authorization or your audio_file in db'

@app.route('/drop', methods=['GET'])
def drop_db():
    db.drop_all()
    return 'Clear'
@app.route('/db', methods=['GET'])
def view_data():
    try:
        users = User.query.all()
        audio_users = Audio.query.all()
    except:
        return 'DB no data'
    else:
        data = [{'id': data.id, 'name': data.user, 'token': str(data.token)} for data in users]
        data_audio = [{'id': audio.id, 'audio': audio.audio_file, 'token': str(audio.token)} for audio in audio_users]
        return jsonify({'db_user': data, 'db_audio': data_audio})

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='127.0.0.1', port=5000)

