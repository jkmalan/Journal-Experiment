from os import path, getenv

defaults = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + path.join(path.dirname(path.abspath(__file__ + '/../../')), 'app.db'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SECRET_KEY': 'SomeSortOfBackupSecretKey',
    'APP_WATSON_ENABLE': True,
    'APP_WATSON_ENTRY': True
}


class Config(object):
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI', defaults['SQLALCHEMY_DATABASE_URI'])
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS', defaults['SQLALCHEMY_TRACK_MODIFICATIONS'])
    SECRET_KEY = getenv('SECRET_KEY', defaults['SECRET_KEY'])
    APP_WATSON_ENABLE = getenv('APP_WATSON_ENABLE', defaults['APP_WATSON_ENABLE'])
    APP_WATSON_ENTRY = getenv('APP_WATSON_ENTRY', defaults['APP_WATSON_ENTRY'])
