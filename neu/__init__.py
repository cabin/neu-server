import os.path

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api
from flask.ext.restful.representations import json

db = SQLAlchemy()

api_mediatype = 'application/neu.v0+json'
restful = Api(prefix='/api', default_mediatype=api_mediatype)
restful.representations[api_mediatype] = json.output_json

PRODUCTION_INSTANCE_PATH = '/srv/www/instance'


def create_app():
    instance_path = None
    if os.path.exists(PRODUCTION_INSTANCE_PATH):
        instance_path = PRODUCTION_INSTANCE_PATH
    app = Flask(
        __name__, instance_relative_config=True, instance_path=instance_path)
    #app.config.update(...)
    app.config.from_pyfile('settings.cfg', silent=True)
    # TODO: Exceptional/Airbrake/Raygun/etc.
    db.init_app(app)
    restful.init_app(app)

    from neu import api
    api.add_resources(restful)

    return app
