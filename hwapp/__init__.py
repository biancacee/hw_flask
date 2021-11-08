import flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

hwapp_obj=flask.Flask(__name__)

hwapp_obj.config.from_mapping( 
        SECRET_KEY='Milo',
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db'),        SQLALCHEMY_TRACK_MODIFICATIONS = False
        )

db = SQLAlchemy(hwapp_obj)

login = LoginManager(hwapp_obj)
login.login_view = 'login'

from hwapp import models, forms, routes
