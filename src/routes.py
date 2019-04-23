from flask import render_template

from src import app
from src import fake_db


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', posts=fake_db.posts)
