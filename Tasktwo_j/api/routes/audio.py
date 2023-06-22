from api.db.session import app
from flask import request
from uuid import uuid4
from api.service.audio import AudioController
from api.db.models.audio import Audio
from api.db.schemas.audio import AudioBase
import pydub


@app.route('/download_audio_file', methods=['GET'])
def download():
    with open('bin_audio.txt', 'wb') as b:
        for i in range(1, 4):
            filename = f'sample-{i}.wav'
            with open(filename, 'rb') as f:
                b.write(f.read())
            print(f'{filename} записан в файл')
        return 'Аудиофайлы записаны'

@app.route('/converting', methods=['POST'])
def converting():
    response = request.get_json()
    token = response['token']
    audio_num = response.get('audio_num')
    if Audio.query(token).filter_by(token=token):
        sound = pydub.AudioSegment.from_wav(f"api/Audio_files/audio_format_wav/sample-{audio_num}.wav")
        sound.export(f"api/Audio_files/audio_format_mp3/sample-{audio_num}.mp3", format='mp3')
        sound_mp3 = pydub.AudioSegment.from_mp3(f"api/Audio_files/audio_format_mp3/sample-{audio_num}.mp3")
        audio_base = AudioBase(audio_file=sound_mp3,
                               token=str(uuid4()))
        audio_cont = AudioController()
        audio_cont.audio_create(audio_base)

@app.route('/unloading_audio_file', methods=['GET'])
def unloading():
    pass

@app.route('/url_download', methods=['GET'])
def url_download():
    pass