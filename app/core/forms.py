from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo, Optional


class SigninForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired()
    ])
    password = PasswordField('Password', validators=[
        InputRequired()
    ])
    remember = BooleanField('Remember')
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired()
    ])
    email = StringField('Email', validators=[
        InputRequired(),
        Email()
    ])
    password = PasswordField('Password', validators=[
        InputRequired(),
        Length(min=8, message='The password must be at least 8 characters')
    ])
    password_verify = PasswordField('Retype Password', validators=[
        InputRequired(),
        EqualTo('password', message='The passwords must be the same')
    ])
    fullname = StringField('Fullname', validators=[
        InputRequired()
    ])
    submit = SubmitField('Submit')


class JournalForm(FlaskForm):
    title = StringField('Journal Title', validators=[
        InputRequired()
    ])
    description = StringField('Journal Description')
    submit = SubmitField('Create')