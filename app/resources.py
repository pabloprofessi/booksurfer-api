import json
from flask_restful import Resource, marshal_with
from flask import request

from . import extensions

from models import Author
from models import Book

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
        response = Author.create(
            json_data['first_name'], 
            json_data['last_name'], 
            json_data['image_url'], 
            json_data['nationality'])
        return response

class AuthorResourceWithId(Resource):

    @marshal_with(Author.simple_fields())
    def get(self, authors_id):
        response = Author.get(authors_id)
        return response

    @marshal_with(Author.simple_fields())
    def put(self, authors_id):
        json_data = request.get_json(force=True)
        response = Author.update(authors_id,
            json_data['first_name'], 
            json_data['last_name'], 
            json_data['image_url'], 
            json_data['nationality'])
        return response

    @marshal_with(Author.simple_fields())
    def delete(self, authors_id):
        response = Author.delete(authors_id)
        return response

class BookResource(Resource):

    @marshal_with(Book.complete_fields())
    def get(self):
        response = Book.query.all()
        return response

    @marshal_with(Book.complete_fields())
    def post(self):
        json_data = request.get_json(force=True)
        response = Book.create(
            json_data['title'], 
            json_data['publisher'], 
            json_data['image_url'], 
            json_data['publish_year'], 
            json_data['editorial'],
            json_data['authors'])
        return response

class BookResourceWithId(Resource):

    @marshal_with(Book.complete_fields())
    def get(self, books_id):
        response = Book.get(books_id)
        return response

    @marshal_with(Book.simple_fields())
    def put(self, books_id):
        json_data = request.get_json(force=True)
        response = Book.update(books_id,
            json_data['title'], 
            json_data['publisher'], 
            json_data['image_url'], 
            json_data['publish_year'], 
            json_data['editorial'])
        return response

    @marshal_with(Book.simple_fields())
    def delete(self, books_id):
        response = Book.delete(books_id)
        return response

extensions.api.add_resource(PingResource, '/ping')
extensions.api.add_resource(AuthorResource, '/authors')
extensions.api.add_resource(AuthorResourceWithId, '/authors/<string:authors_id>')
extensions.api.add_resource(BookResource, '/books')
extensions.api.add_resource(BookResourceWithId, '/books/<string:books_id>')

