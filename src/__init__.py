from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'f2c80b32f536165d6a57ed9cb08a84a4'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'              # if login required redierct to login
login_manager.login_message_category = 'info'   # class bootstrap for div flashs


from src import routes
from src.models import *
