from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask
import os

app = Flask(__name__)
app.config['DEBUG'] = True

db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')
db_host = os.environ.get('DB_HOST')

#app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:(...)@localhost:5432/project2"
=======
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:tarawater@localhost:5432/project2"
>>>>>>> 8a8dec806f7cc7bd77d59d0acfb3ce318fa09527
db = SQLAlchemy(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
