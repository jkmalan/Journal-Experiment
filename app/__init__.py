from flask import Flask

from app.core.config import Config


def create_app():
    app = Flask(__name__)

    # Initialize configuration options
    app.config.from_object(Config)

    # Initialize global containers
    from app.core import db, bc, lm
    db.init_app(app)
    bc.init_app(app)
    lm.init_app(app)
    lm.login_view = 'bp.signin'

    print("Load blueprints")
    # Initialize app routes
    from app.core import bp
    app.register_blueprint(bp)

    return app
