from os import path


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(path.dirname(path.abspath(__file__ + '/../../')), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ReplaceMeWithARealSecretKey'


config = Config()
