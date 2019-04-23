from flask import render_template

from src import app
from src import fake_db
from src import forms


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', posts=fake_db.posts)


@app.route("/login")
def login():
    return render_template('login.html', form=forms.LoginForm())
