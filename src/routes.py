from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required

from src import app
from src import forms
from src.models import *




@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', posts=get_posts())


@app.route("/login", methods=['GET', 'POST'])
def login():
    # if user login before, redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # form created by flask_wtf
    form = forms.LoginForm()
    # if user click on submit button and no error validation
    if form.validate_on_submit():
        # get user filter by username
        user = User.query.filter_by(username=form.username.data).first()
        if user and form.password.data==user.password:
            login_user(user, remember=form.remember.data)
            flash("you are login", 'success')
            return redirect(url_for('index'))
        else:
            flash("username or password not correct", 'danger')

    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    form = forms.PostForm()
    if form.validate_on_submit():
        post = set_post(form.title.data, form.content.data)
        flash("new post addes", 'success')
        return redirect(url_for('index'))
    return render_template('create.html', form=form)
