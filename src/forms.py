from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo



class LoginForm(FlaskForm):
    username = StringField('اسم المستخدم', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('كلمة المرور', validators=[DataRequired()])
    remember = BooleanField('تذكرني')
    submit = SubmitField('دخول')