import functools

from flask import request
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


class ArgumentFromJson(reqparse.Argument):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = ('json', 'values')
        super(ArgumentFromJson, self).__init__(*args, **kwargs)


prospects = []  # XXX for deployment testing only; resets on server restart

class ProspectList(Resource):
    parser = reqparse.RequestParser(ArgumentFromJson)

    def post(self):
        prospect = self.parser.parse_args()
        prospect['ip'] = request.remote_addr
        prospects.append(prospect)
        return prospect, 201

ProspectList.parser.add_argument('name', required=True)
ProspectList.parser.add_argument('email', required=True)
ProspectList.parser.add_argument('zip')
ProspectList.parser.add_argument('note')


class AdminProspectList(Resource):
    method_decorators = [authenticate]
    parser = ProspectList.parser

    def get(self):
        return prospects


def add_resources(api):
    api.add_resource(ProspectList, '/prospects')
    api.add_resource(AdminProspectList, '/admin/prospects')
