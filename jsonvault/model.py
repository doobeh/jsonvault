from datetime import datetime
from .utilities import generate_key
from .database import db


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, project_name):
        self.name = project_name

    def __repr__(self):
        return self.name


class Token(db.Model):
    __tablename__ = 'token'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, unique=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('tokens', lazy=True))

    def __init__(self, project):
        self.token = generate_key()
        self.project = project

    def __repr__(self):
        return self.token


class Vault(db.Model):
    __tablename__ = 'vault'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('vaults', lazy=True))

    def __init__(self, project, data):
        self.project = project
        self.data = data

    def __repr__(self):
        return self.data
