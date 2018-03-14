import click
from flask_sqlalchemy import SQLAlchemy
from flask.cli import AppGroup, FlaskGroup
from jsonvault.model import Token, Vault, Project
from jsonvault.database import db


project_cli = AppGroup('project')
token_cli = AppGroup('token')
db_cli = AppGroup('db')


@db_cli.command('init')
def db_init_command():
    """Creates the database tables."""
    db.create_all()
    print('Initialized the database.')


@db_cli.command('drop')
def db_drop_command():
    """Drops the database tables."""
    db.drop_all()
    print('Dropped the database.')


@project_cli.command('create')
@click.argument('name')
def project_add_command(name):
    project = Project(name)
    db.session.add(project)
    db.session.commit()


@token_cli.command('create')
@click.argument('projectid', type=int)
def token_add_command(projectid):
    p = Project.query.filter_by(id=projectid).first()
    if p:
        t = Token(p)
        print('Token Added: {}'.format(t.token))
        db.session.add(t)
        db.session.commit()
    else:
        print('Project Not Found-- Pick one from below')
        existing = Project.query.all()
        for project in existing:
            print(f'[{project.id}] - {project.name}')