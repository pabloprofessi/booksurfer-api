import json
from flask_restful import Resource, marshal_with
from flask import request

from . import extensions

from models import Author
#from models import Book

class PingResource(Resource):

    def get(self):
        return "pong"
class AuthorResource(Resource):

    @marshal_with(Author.simple_fields())
    def get(self):
        response = Author.query.all()
        return response


extensions.api.add_resource(PingResource, '/ping')
extensions.api.add_resource(AuthorResource, '/authors')
