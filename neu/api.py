import functools

import flask.ext.restful
from flask.ext.restful import abort, reqparse, Resource


# Monkeypatch unauthorized responses to not send a `WWW-Authenticate` header,
# which causes browsers to pop up an authentication dialog.
# See <https://github.com/twilio/flask-restful/issues/83>.
def unauthorized_no_authenticate_header(response, realm):
    return response
flask.ext.restful.unauthorized = unauthorized_no_authenticate_header


def authenticate(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if True:  # XXX
            return fn(*args, **kwargs)
        abort(401)
    return wrapper


prospects = []  # XXX for deployment testing only; resets on server restart

class ProspectList(Resource):
    parser = reqparse.RequestParser()

    def post(self):
        prospect = self.parser.parse_args()
        prospects[len(prospects)] = prospect
        return prospect, 201

ProspectList.parser.add_argument('name', required=True)
ProspectList.parser.add_argument('email', required=True)


class AdminProspectList(Resource):
    method_decorators = [authenticate]
    parser = ProspectList.parser

    def get(self):
        return prospects


def add_resources(api):
    api.add_resource(ProspectList, '/prospects')
    api.add_resource(AdminProspectList, '/admin/prospects')
