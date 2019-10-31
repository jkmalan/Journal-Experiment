from flask import request, render_template, url_for, redirect
from flask_login import current_user, login_required, login_user, logout_user

from app.api.watson import analyze
from app.core import bp
from app.core.forms import SigninForm, SignupForm
from app.core.models import User, Journal, Entry


@bp.route('/', methods=['GET'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('bp.user_view'))
    return render_template('home.html')


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('bp.home'))

    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.match_password(password=form.password.data):
            return redirect(url_for('bp.signin'))

        login_user(user, remember=form.remember.data)

        navigate = request.args.get('return_url')
        if not navigate:
            navigate = url_for('bp.home')

        return redirect(navigate)
    return render_template('signin.html', form=form)


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('bp.home'))

    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data,
            fullname=form.fullname.data,
            email=form.email.data
        )
        user.store_password(form.password.data)
        user.create()

        return redirect(url_for('bp.signin'))
    return render_template('signup.html', form=form)


@bp.route('/signout', methods=['GET'])
@login_required
def signout():
    logout_user()
    return render_template('signout.html')


@bp.route('/user', methods=['GET', 'POST'])
@login_required
def user_view():
    user = current_user

    if request.method == 'POST':
        title = request.form.get('journal_title')
        user.create_journal(title=title)

    journal = user.get_journal()
    return render_template('user.html', user=user, journal=journal)


@bp.route('/user/journal', methods=['GET', 'POST'])
@login_required
def journal_view():
    user = current_user
    journal = Journal.query.filter_by(user_id=user.id).first()

    if request.method == 'POST':
        title = request.form.get('entry_title')
        body = request.form.get('entry_body')
        journal.add_entry(title=title, body=body)

    entries = journal.get_entries()
    return render_template('journal.html', journal=journal, entries=entries)


@bp.route('/user/journal/entry/<int:entry_id>', methods=['GET', 'POST'])
@login_required
def entry_view(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first()
    emotions = entry.get_emotions()
    if len(emotions) == 0:
        emotion = analyze(entry.body)
        for key, value in emotion.items():
            entry.add_emotion(name=key, value=value)

    emotions = entry.get_emotions()
    return render_template('entry.html', entry=entry, emotions=emotions)
