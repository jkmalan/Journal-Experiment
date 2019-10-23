from flask import Blueprint, request, render_template, url_for, redirect, session

from app.core.model import model, User, Journal, Entry

route = Blueprint('route', __name__, template_folder='../web')


@route.route('/', methods=['GET'])
def home():
    data = str(session.items())
    print(data)
    return render_template('home.html')


@route.route('/signin', methods=['GET'])
def signin():
    data = str(session.items())
    print(data)
    return render_template('signin.html')


@route.route('/signup', methods=['GET'])
def signup():
    data = str(session.items())
    print(data)
    return render_template('signup.html')


@route.route('/user', methods=['GET'])
def user():
    data = str(session.items())
    print(data)
    return render_template('user.html')


@route.route('/journal', methods=['GET'])
def journal():
    data = str(session.items())
    print(data)
    return render_template('journal.html')


@route.route('/journal/entry', methods=['GET'])
def entry():
    data = str(session.items())
    print(data)
    return render_template('entry.html')


@route.route('/auth/signin', methods=['POST'])
def auth_signin():
    username = request.form.get('username')
    password = request.form.get('password')

    guest = User.query.filter_by(username=username).first()
    if guest is not None:
        if guest.password == password:
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

    return redirect(url_for('route.user'))
