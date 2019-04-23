from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'f2c80b32f536165d6a57ed9cb08a84a4'

db = SQLAlchemy(app)



from src import routes
# from src.models import *
