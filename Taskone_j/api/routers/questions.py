from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/questions', methods=['POST'])
def generate_questions():
    pass

@app.route('/get_questions', methods=['GET'])
def get_questions():
    pass