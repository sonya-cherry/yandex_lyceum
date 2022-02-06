from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class LoginForm(FlaskForm):
    email = StringField(label='email:')
    password = PasswordField()
    remember_me =
    submit = SubmitField()