from flask import Flask
from flask_cors import CORS
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

flaskApp = Flask(__name__)
flaskApp.config['SECRET_KEY'] = 'cits5505'
CORS(flaskApp)  # enable CORS on all routes
flaskApp.config.from_object(Config)  # Load all configurations from Config class, including SECRET_KEY

db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db)
login = LoginManager(flaskApp)
login.login_view = 'index'  # route for index.html

from app import routes, model, gameplay
from app.model import Person

@login.user_loader
def load_user(id):
    return Person.query.get(int(id))
