"""
    JsonVault
    ~~~~~~
    Log JSON to process later.
    :copyright: (c) 2018 by Anthony Plunkett.
    :license: BSD, see LICENSE for more details.
"""

import os
from flask import Flask
from .database import db
from .model import Token, Project, Vault
from cli import project_cli, token_cli, db_cli, core_cli
from jsonvault.api import api
from flask_cors import CORS


def create_app(config=None):
    app = Flask('jsonvault')

    app.config.update(dict(
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'jsonvault.sqlite3'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=True,
        SECRET_KEY=b'OHNOES!',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.update(config or {})
    app.config.from_envvar('JSONVAULT_SETTINGS', silent=True)
    db.init_app(app)
    register_cli(app)
    app.register_blueprint(api)
    CORS(app)

    return app


def register_cli(app):
    app.cli.add_command(project_cli)
    app.cli.add_command(token_cli)
    app.cli.add_command(db_cli)
    app.cli.add_command(core_cli)


