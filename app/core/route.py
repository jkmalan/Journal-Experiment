import os

from flask import Blueprint, request, flash, render_template, url_for, redirect, session
from functools import wraps

from app.api.watson import analyze
from app.core.model import model, User, Journal, Entry

route = Blueprint('route', __name__, template_folder='../web')


@route.route('/auth/signin', methods=['POST'])
def auth_signin():
    username = request.form.get('username')
    password = request.form.get('password')

    guest = User.query.filter_by(username=username).first()
    if guest is not None:
        if guest.password == password:
            session['user_id'] = guest.id
            return redirect(url_for('route.user'))

    return redirect(url_for('route.home'))


@route.route('/auth/signup', methods=['POST'])
def auth_signup():
    username = request.form.get('username')
    password = request.form.get('password')
    fullname = request.form.get('fullname')
    email = request.form.get('email')

    guest = User(username=username, password=password, fullname=fullname, email=email)
    model.session.add(guest)
    model.session.commit()

    guest = User.query.filter_by(username=username).first()
    session['user_id'] = guest.id
    return redirect(url_for('route.user'))


def auth_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id:
            guest = User.query.filter_by(id=user_id)
            if guest:
                return function(*args, **kwargs)

        return redirect(url_for('route.signin'))
    return wrapper


@route.route('/', methods=['GET'])
def home():
    if session['user_id'] is not None:
        return redirect(url_for('route.user'))
    return render_template('home.html')


@route.route('/signin', methods=['GET'])
def signin():
    return render_template('signin.html')


@route.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@route.route('/signout', methods=['GET'])
def signout():
    session['user_id'] = None
    return render_template('signout.html')


@route.route('/user', methods=['GET'])
@auth_required
def user():
    return render_template('user.html')


@route.route('/journal', methods=['GET'])
@auth_required
def journal():
    return render_template('journal.html')


@route.route('/journal/entry', methods=['GET'])
@auth_required
def entry():
    return render_template('entry.html')
