from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask
import os

app = Flask(__name__)

db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')
db_host = os.environ.get('DB_HOST')

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:{os.getenv('DB_PASSWORD')}@localhost:5432/project2"
#pp.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"

db = SQLAlchemy(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

