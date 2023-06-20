from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Audio(db.Model):
    __tablename__ = 'audio'
    id = db.Column(db.Integer, primary_key=True)
    audio_file = db.Column(db.String)
    token = db.Column(db.String)
