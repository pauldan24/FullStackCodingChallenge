
from flask import Flask                     #import flask module
from app.views.home import home
from app.models import Card, Deck

def create_app():
    app = Flask(__name__)

    app.config.update(
        DEBUG = True,
        SECRET_KEY = 'secret_xxx'
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



    app.register_blueprint(home)

    return app
