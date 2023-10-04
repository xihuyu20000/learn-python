import importlib

from flask import Flask, Blueprint

from basic._db import db
from config import config


def auto_register_plugins(app):
    mod = importlib.import_module('plugins.core.routes')
    bp:Blueprint = mod.bp
    app.register_blueprint(bp)


def create_app(config_name=None):
    app = Flask('flask-sqlalchemy-pytest')

    app.config.from_object(config[config_name]())

    db.init_app(app)

    auto_register_plugins(app)
    @app.route('/hello')
    def hello():
        return 'hello'

    return app