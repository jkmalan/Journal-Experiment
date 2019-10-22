from flask import Flask

from app.core.config import config
from app.core.model import model
from app.core.route import route


def initialize():
    me = Flask(__name__)

    # Initialize configuration options
    me.config.from_object(config)

    # Initialize data models
    model.init_app(me)
    with me.app_context():
        model.create_all()

    # Initialize app routes
    me.register_blueprint(route)

    return me


app = initialize()
