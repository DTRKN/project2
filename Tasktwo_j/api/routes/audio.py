from api.db.session import app
from flask import request
from uuid import uuid4
from api.service.audio import AudioController
from api.db.models.audio import Audio
from api.db.schemas.audio import AudioBase
from api.service.user import UserController
import pydub


@app.route('/Adding_audio_file', methods=['POST'])
def Adding_audio_file():
    response = request.get_json()
    id_user = response['id']
    token = response['token']
    audio_file = response.get('audio_file')
    audio_name = audio_file.split('.')[0]

    if Audio.query.filter_by(token=token):
        sound = pydub.AudioSegment.from_wav(f"api/Audio_files/audio_format_wav/{audio_file}")
        sound.export(f"api/Audio_files/audio_format_mp3/{audio_name}.mp3", format='mp3')
        sound_mp3 = pydub.AudioSegment.from_mp3(f"api/Audio_files/audio_format_mp3/{audio_name}.mp3")
        audio_base = AudioBase(audio_file=sound_mp3.raw_data,
                               token=str(uuid4()))

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

