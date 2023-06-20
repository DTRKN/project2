from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/create_user', methods=['POST'])
def create_user():
    pass