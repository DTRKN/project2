from db.session import app
from flask import request
from uuid import uuid4
from service.audio import AudioController
from db.models.user import User
from db.schemas.audio import AudioBase
from service.user import UserController
from db.session import db
from pydub import AudioSegment
import os

@app.route('/Adding_audio_file', methods=['POST'])
def Adding_audio_file():
    response = request.get_json()
    id_user = response['id']
    token = response['token']
    audio_file = response.get('audio_file')
    audio_name = audio_file.split('.')[0]

    audio_wav_path = f"api/Audio_files/audio_format_wav/{audio_file}"
    audio_mp3_path = f"api/Audio_files/audio_format_mp3/{audio_name}.mp3"

    if db.session().query(User).filter_by(token=token):
        AudioSegment.ffmpeg = "/absolute/path/to/ffmpeg"
        if not os.path.isfile(audio_mp3_path):
            sound = AudioSegment.from_wav(audio_wav_path)
            sound.export(audio_mp3_path, format='mp3')

        with open(audio_mp3_path, 'rb') as f:
            audio_base = AudioBase(audio_file=f.read(), token=str(uuid4()))
        print(audio_base)

        audio_cont = AudioController()
        audio_file = audio_cont.audio_create(audio_base)

        return f'http://localhost/record?id={audio_file}&user={id_user}'


@app.route(f'/record?id=<id_audio_file>&user=<id_user>',  methods=['GET'])
def url_download(id_audio_file, id_user):
    user_cont = UserController()
    user_cont.get_user_id(id_user)
    audio_cont = AudioController()
    audio_file = audio_cont.get_audio_file(id_audio_file)
    return audio_file

