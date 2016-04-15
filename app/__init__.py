#!/usr/bin/env python
from flask import Flask
from config import config


# Factory to create a Flask app
def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app.api_1_0.fibAPI import api as fib_api
    app.register_blueprint(fib_api, url_prefix='/api/v1.0')

    return app
