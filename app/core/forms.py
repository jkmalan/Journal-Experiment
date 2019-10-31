from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class SigninForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired()
    ])
    password = PasswordField('Password', validators=[
        DataRequired()
    ])
    remember = BooleanField('Remember')
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired()
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message='The password must be at least 8 characters')
    ])
    password_verify = PasswordField('Password Verify', validators=[
        DataRequired(),
        EqualTo('password')
    ])
    fullname = StringField('Fullname', validators=[
        DataRequired()
    ])
    submit = SubmitField('Submit')

