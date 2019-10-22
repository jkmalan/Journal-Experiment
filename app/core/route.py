import datetime

from flask import Blueprint, request, render_template, session

from app.core.model import model, User, Journal, Entry

route = Blueprint('route', __name__, template_folder='../web')


@route.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username)
        if user & user.password == password:
            return dash(user)
        else:
            return render_template('index.html')

    return render_template('index.html')


@route.route('/api/auth/signin', methods=['POST'])
def signin():

    return ''


@route.route('/dash')
def dash():
    data = str(session.items())


    return render_template('user.html')