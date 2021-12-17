from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import views, models
from app.models import *
login_manager= LoginManager()
login_manager.login_view="UserSignIn"
login_manager.init_app(app)
login_manager.login_message="User logged in"
@login_manager.user_loader
def load_user(id):
    return Sign_In.query.get(int(id))
