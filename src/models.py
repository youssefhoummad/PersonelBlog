from datetime import datetime

from src import db, login_manager
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    username_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    username = db.relationship('User',
        backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title




# some function to maniplt db
def get_users():
    return User.query.all()

def get_posts():
    return Post.query.all()


@login_manager.user_loader
def get_user(user_id):
    return User.query.get(int(user_id))

def set_user(username, email, password):
    db.session.add(User(username=username, email=email, password=password))
    db.session.commit()


def set_post(title, content, username_id=None):
    db.session.add(Post(title=title, content=content, \
                        username_id=int(username_id) if username_id else 1))
    db.session.commit()
