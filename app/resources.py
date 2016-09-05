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
    def get(self, author_id):
        response = Author.get(author_id)
        return response

    @marshal_with(Author.simple_fields())
    def put(self, author_id):
        json_data = request.get_json(force=True)
        response = Author.update(author_id,
            json_data['first_name'], 
            json_data['last_name'], 
            json_data['image_url'], 
            json_data['nationality'])
        return response

    @marshal_with(Author.simple_fields())
    def delete(self, author_id):
        response = Author.delete(author_id)
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
    def get(self, book_id):
        response = Book.get(book_id)
        return response

    @marshal_with(Book.simple_fields())
    def put(self, book_id):
        json_data = request.get_json(force=True)
        response = Book.update(book_id,
            json_data['title'], 
            json_data['publisher'], 
            json_data['image_url'], 
            json_data['publish_year'], 
            json_data['editorial'])
        return response

    @marshal_with(Book.simple_fields())
    def delete(self, book_id):
        response = Book.delete(book_id)
        return response



class SampleResource(Resource):

    @marshal_with(Sample.simple_fields())
    def get(self):
        response = Sample.query.all()
        return response

    @marshal_with(Sample.simple_fields())
    def post(self):
        json_data = request.get_json(force=True)
        response = Sample.create(
            json_data['first_name'], 
            json_data['last_name'], 
            json_data['image_url'], 
            json_data['nationality'])
        return response

class SampleResourceWithId(Resource):

    @marshal_with(Sample.simple_fields())
    def get(self, sample_id):
        response = Sample.get(sample_id)
        return response

    @marshal_with(Sample.simple_fields())
    def put(self, sample_id):
        json_data = request.get_json(force=True)
        response = Sample.update(sample_id,
            json_data['first_name'], 
            json_data['last_name'], 
            json_data['image_url'], 
            json_data['nationality'])
        return response

    @marshal_with(Sample.simple_fields())
    def delete(self, sample_id):
        response = Sample.delete(sample_id)
        return response

extensions.api.add_resource(PingResource, '/ping')
extensions.api.add_resource(AuthorResource, '/authors')
extensions.api.add_resource(AuthorResourceWithId, '/authors/<string:author_id>')
extensions.api.add_resource(BookResource, '/books')
extensions.api.add_resource(BookResourceWithId, '/books/<string:book_id>')
extensions.api.add_resource(SampleResource, '/books/<string:book_id>/samples')
extensions.api.add_resource(SampleResourceWithId, '/books/<string:book_id>/samples/<string:sample_id>')

