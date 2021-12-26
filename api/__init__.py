from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from .v1 import v1 as v1_blueprint
from flask_restful import Api

db = SQLAlchemy()
api = Api()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.register_blueprint(v1_blueprint)

    db.init_app(app)
    api.init_app(app)

    return app
