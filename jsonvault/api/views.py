from . import api
from flask import request, abort, jsonify, json, current_app
from jsonvault.model import Project, Vault, Token
from jsonvault.database import db


@api.route('/<project>/store/', methods=['POST'])
def store(project):
    if request.is_json:
        data = request.get_json()
        p = Project.query.filter_by(name=project).first()
        user_token = data.get('token')
        if not user_token:
            abort(401)
        existing_token = Token.query.filter_by(token=user_token).first()
        if existing_token and existing_token.project == p:
            user_json = json.dumps(data.get('data'))
            vault = Vault(p, user_json)
            db.session.add(vault)
            db.session.commit()
            return jsonify({'message': 'added data'})
    else:
        abort(400)


@api.route('/<project>/')
def view(project):
    p = Project.query.filter_by(name=project).first()
    if not p:
        return abort(404)

    response = current_app.response_class(
        response="[{}]".format(",".join([x.data for x in p.vaults])),
        status=200,
        mimetype='application/json'
    )
    return response
