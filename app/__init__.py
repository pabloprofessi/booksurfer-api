import os

from flask import Flask
from flask_cors import CORS, cross_origin


from . import extensions, resources


def create_app(environment='dev'):
    app = Flask('booksurfer-api')
    app.config['DEBUG'] = True
    app.log.setLevel('DEBUG') 
    CORS(app)

    app.config.from_pyfile('config/{}.py'.format(environment))

    extensions.db.init_app(app)
    extensions.api.init_app(app)

    with app.app_context():
        extensions.db.create_all()

    return app
