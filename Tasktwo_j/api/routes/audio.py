import base64
import binascii
import zlib

from db.session import app
from flask import request, jsonify
from uuid import uuid4
from service.audio import AudioController
from db.models.user import User
from db.schemas.audio import AudioBase
from service.user import UserController
from db.base_class import Base
from db.session import db, engine
from pydub import AudioSegment
import os

@app.route('/Adding_audio_file', methods=['POST'])
def Adding_audio_file():

    Base.metadata.create_all(engine)

    response = request.get_json()
    id_user = response['id']
    token = response['token']
    audio_file = response.get('audio_file')
    audio_name = audio_file.split('.')[0]

    audio_wav_path = f"api/Audio_files/audio_format_wav/{audio_file}"
    audio_mp3_path = f"api/Audio_files/audio_format_mp3/{audio_name}.mp3"

    user = db.session().query(User).filter_by(id=id_user, token=token).first()

    if user:
        AudioSegment.ffmpeg = "/absolute/path/to/ffmpeg"
        if not os.path.isfile(audio_mp3_path):
            sound = AudioSegment.from_wav(audio_wav_path)
            sound.export(audio_mp3_path, format='mp3')

        sound_mp3 = AudioSegment.from_mp3(audio_mp3_path)
        raw_audio_data = sound_mp3.raw_data
        binary_string = binascii.b2a_base64(raw_audio_data)

        audio_base = AudioBase(audio_file=binary_string[:30], token=str(uuid4()))
        audio_cont = AudioController()
        audio_id = audio_cont.audio_create(audio_base)

        return f'http://127.0.0.1:5000/record/id={audio_id[0]}/user={id_user}'
    else:
        return 'User not found'

@app.route('/record/id=<id_audio_file>/user=<id_user>',  methods=['GET'])
def url_download(id_audio_file, id_user):
    user_cont = UserController()
    user_cont.get_user_id(id_user)
    audio_con = AudioController()
    audio_file = audio_con.get_audio_file_id(id_audio_file)

    return jsonify({"url_audio_mp3": audio_file[0]})
@app.route('/view_audio', methods=['GET'])
def view_audio():
    audio_cont = AudioController()
    audio = audio_cont.view_audio()
    return audio