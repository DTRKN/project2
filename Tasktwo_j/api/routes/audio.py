from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/download_audio_file', methods=['POST'])
def download():
    pass

@app.route('/converting', methods=['POST'])
def converting():
    pass

@app.route('/unloading_audio_file', methods=['GET'])
def unloading():
    pass