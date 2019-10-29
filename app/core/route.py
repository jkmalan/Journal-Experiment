import os

from flask import Blueprint, request, flash, render_template, url_for, redirect, session
from functools import wraps

from app.api.watson import analyze
from app.core.config import config
from app.core.model import model, User, Journal, Entry

route = Blueprint('route', __name__, template_folder='../web')


@route.route('/auth/signin', methods=['POST'])
def auth_signin():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user is not None:
        if user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('route.user_view'))

    return redirect(url_for('route.home'))


@route.route('/auth/signup', methods=['POST'])
def auth_signup():
    username = request.form.get('username')
    password = request.form.get('password')
    fullname = request.form.get('fullname')
    email = request.form.get('email')

    user = User(username=username, password=password, fullname=fullname, email=email)
    model.session.add(user)
    model.session.commit()

    user = User.query.filter_by(username=username).first()
    session['user_id'] = user.id
    return redirect(url_for('route.user_view'))


def auth_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.filter_by(id=user_id)
            if user:
                return function(*args, **kwargs)

        return redirect(url_for('route.signin'))
    return wrapper


@route.route('/', methods=['GET'])
def home():
    if session.get('user_id'):
        return redirect(url_for('route.user_view'))
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


@route.route('/user', methods=['GET', 'POST'])
@auth_required
def user_view():
    user = User.query.filter_by(id=session.get('user_id')).first()

    if request.method == 'POST':
        title = request.form.get('journal_title')
        user.create_journal(title=title)

    journal = user.get_journal()
    return render_template('user.html', user=user, journal=journal)


@route.route('/user/journal', methods=['GET', 'POST'])
@auth_required
def journal_view():
    journal = Journal.query.filter_by(user_id=session.get('user_id')).first()

    if request.method == 'POST':
        title = request.form.get('entry_title')
        body = request.form.get('entry_body')
        journal.add_entry(title=title, body=body)

    entries = journal.get_entries()
    return render_template('journal.html', journal=journal, entries=entries)


@route.route('/user/journal/entry/<int:entry_id>', methods=['GET', 'POST'])
@auth_required
def entry_view(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first()
    emotions = entry.get_emotions()
    if not emotions:
        emotion = analyze(entry.body)
        for key, value in emotion.items():
            entry.add_emotion(name=key, value=value)

    emotions = entry.get_emotions()
    return render_template('entry.html', entry=entry, emotions=emotions)
