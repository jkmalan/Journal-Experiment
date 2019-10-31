from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bc = Bcrypt()
lm = LoginManager()

bp = Blueprint('bp', __name__, template_folder='../web')

from app.core import models
from app.core import routes
