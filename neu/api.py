import functools

from flask import request
import flask.ext.restful
from flask.ext.restful import abort, fields, marshal_with, reqparse, Resource

from neu import db
from neu.models import Prospect, Rfi


# Monkeypatch unauthorized responses to not send a `WWW-Authenticate` header,
# which causes browsers to pop up an authentication dialog.
# See <https://github.com/twilio/flask-restful/issues/83>.
def unauthorized_no_authenticate_header(response, realm):
    return response
flask.ext.restful.unauthorized = unauthorized_no_authenticate_header


class ArgumentFromJson(reqparse.Argument):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = ('json', 'values')
        super(ArgumentFromJson, self).__init__(*args, **kwargs)


prospect_fields = {
    'type': fields.String,
    'name': fields.String,
    'email': fields.String,
    'zip': fields.String(attribute='zipcode'),
    'note': fields.String,
    'created_at': fields.DateTime,
}


class ProspectList(Resource):
    parser = reqparse.RequestParser(ArgumentFromJson)

    @marshal_with(prospect_fields)
    def post(self):
        prospect = Prospect(**self.parser.parse_args())
        prospect.ip_address = request.remote_addr
        db.session.add(prospect)
        db.session.commit()
        return prospect, 201

ProspectList.parser.add_argument('type')
ProspectList.parser.add_argument('name', required=True)
ProspectList.parser.add_argument('email', required=True)
ProspectList.parser.add_argument('zip', dest='zipcode')
ProspectList.parser.add_argument('note')


rfi_fields = {
    'type': fields.String,
    'fname': fields.String,
    'lname': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'zip': fields.String(attribute='zipcode'),
    'note': fields.String,
    'subscribed': fields.Boolean,
    'created_at': fields.DateTime,
}


class RfiList(Resource):
    parser = reqparse.RequestParser(ArgumentFromJson)

    @marshal_with(rfi_fields)
    def post(self):
        rfi = Rfi(**self.parser.parse_args())
        db.session.add(rfi)
        db.session.commit()
        return rfi, 201

RfiList.parser.add_argument('type', required=True)
RfiList.parser.add_argument('fname', required=True)
RfiList.parser.add_argument('lname', required=True)
RfiList.parser.add_argument('email', required=True)
RfiList.parser.add_argument('phone')
RfiList.parser.add_argument('zip', dest='zipcode')
RfiList.parser.add_argument('note')
RfiList.parser.add_argument('subscribed', type=bool)
RfiList.parser.add_argument('maker_faire', type=bool)


#def authenticate(fn):
#    @functools.wraps(fn)
#    def wrapper(*args, **kwargs):
#        if True:  # XXX
#            return fn(*args, **kwargs)
#        abort(401)
#    return wrapper
#
#
#class AdminProspectList(Resource):
#    method_decorators = [authenticate]
#
#    @marshal_with(prospect_fields)
#    def get(self):
#        return Prospect.query.all()


def add_resources(api):
    api.add_resource(ProspectList, '/prospects')
    api.add_resource(RfiList, '/rfi')
    #api.add_resource(AdminProspectList, '/admin/prospects')
