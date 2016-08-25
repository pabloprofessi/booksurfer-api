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

    @marshal_with(Author.simple_fields())
    def post(self):
        json_data = request.get_json(force=True)
        response = Author.create(json_data['first_name'], json_data['last_name'], json_data['image_url'], json_data['nationality'])
        return response

class AuthorResourceWithId(Resource):

    @marshal_with(Author.simple_fields())
    def get(self, authors_id):
        response = Author.get(authors_id)
        return response

    @marshal_with(Author.simple_fields())
    def put(self, authors_id):
        json_data = request.get_json(force=True)
        response = Author.update(authors_id,json_data['first_name'], json_data['last_name'], json_data['image_url'], json_data['nationality'])
        return response

    @marshal_with(Author.simple_fields())
    def delete(self, authors_id):
        response = Author.delete(authors_id)
        return response

extensions.api.add_resource(PingResource, '/ping')
extensions.api.add_resource(AuthorResource, '/authors')
extensions.api.add_resource(AuthorResourceWithId, '/authors/<string:authors_id>')

