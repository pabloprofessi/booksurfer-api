import json
from flask_restful import Resource, marshal_with
from flask import request

from . import extensions

from models import Author
from models import Book
from models import Sample
from models import Member
from models import Loan

class PingResource(Resource):
    def get(self):
        return "pong"

class AuthorResource(Resource):

    @marshal_with(Author.complete_fields())
    def get(self):
        response = Author.query.all()
        return response

    @marshal_with(Author.simple_fields())
    def post(self):
        json_data = request.get_json(force=True)
        response = Author.create(
            json_data['firstName'], 
            json_data['lastName'], 
            json_data['nationality'])
        return response

class AuthorResourceWithId(Resource):

    @marshal_with(Author.complete_fields())
    def get(self, author_id):
        response = Author.get(author_id)
        return response

    @marshal_with(Author.simple_fields())
    def put(self, author_id):
        json_data = request.get_json(force=True)
        response = Author.update(author_id,
            json_data['firstName'], 
            json_data['lastName'], 
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
            json_data['editionYear'], 
            json_data['editionCountry'], 
            json_data['price'],
            json_data['isbn'],
            json_data['reputationValue'],
            json_data['loanType'])
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
            json_data['editionYear'], 
            json_data['editionCountry'], 
            json_data['price'],
            json_data['isbn'],
            json_data['reputationValue'],
            json_data['loanType'])
        return response

    @marshal_with(Book.simple_fields())
    def delete(self, book_id):
        response = Book.delete(book_id)
        return response


class SampleResource(Resource):

    @marshal_with(Sample.complete_fields())
    def get(self):
        response = Sample.query.all()
        return response

    @marshal_with(Sample.simple_fields())
    def post(self):
        json_data = request.get_json(force=True)
        response = Sample.create(
            json_data['bookId'],
            json_data['acquisitionDate'], 
            json_data.get('discardDate',None), 
            json_data['barCode'])
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
                json_data['acquisitionDate'], 
                json_data.get('discardDate',None),
                json_data['barCode'])

        return response

    @marshal_with(Sample.simple_fields())
    def delete(self, sample_id):
        response = Sample.delete(sample_id)
        return response


class MemberResource(Resource):

    @marshal_with(Member.simple_fields())
    def get(self):
        response = Member.query.all()
        return response

    @marshal_with(Member.simple_fields())
    def post(self):
        json_data = request.get_json(force=True)
        response = Member.create(            
            json_data['firstName'],
            json_data['lastName'],
            json_data['dni'],
            json_data['nationality'],
            json_data['cuil'],
            json_data['phone'],
            json_data['email'],
            json_data['zipCode'],
            json_data['city'],
            json_data['state'],
            json_data['enabled'])
        return response

class MemberResourceWithId(Resource):

    @marshal_with(Member.simple_fields())
    def get(self, member_id):
        response = Member.get(member_id)
        return response

    @marshal_with(Member.simple_fields())
    def put(self, member_id):
        json_data = request.get_json(force=True)
        response = Member.update(member_id,
            json_data['firstName'],
            json_data['lastName'],
            json_data['dni'],
            json_data['nationality'],
            json_data['cuil'],
            json_data['phone'],
            json_data['email'],
            json_data['zipCode'],
            json_data['city'],
            json_data['state'],
            json_data['enabled'])
        return response

    @marshal_with(Member.simple_fields())
    def delete(self, member_id):
        response = Member.delete(member_id)
        return response



class LoanResource(Resource):

    @marshal_with(Loan.simple_fields())
    def get(self):
        response = Loan.query.all()
        return response

    @marshal_with(Loan.simple_fields())
    def post(self):
        json_data = request.get_json(force=True)
        response = Loan.create(
            json_data['memberId'],
            json_data['sampleId'],
            json_data['agreedReturnDate'],
            json_data['returnDate'],
            json_data['withdrawDate'],
            json_data['comment'],
            json_data['loanType'])
        return response

class LoanResourceWithId(Resource):

    @marshal_with(Loan.simple_fields())
    def get(self, loan_id):
        response = Loan.get(loan_id)
        return response

    @marshal_with(Loan.simple_fields())
    def put(self, loan_id):
        json_data = request.get_json(force=True)
        response = Loan.update(loan_id,
            json_data['memberId'],
            json_data['sampleId'],
            json_data['agreedReturnDate'],
            json_data['returnDate'],
            json_data['withdrawDate'],
            json_data['comment'],
            json_data['loanType'])
        return response

    @marshal_with(Loan.simple_fields())
    def delete(self, loan_id):
        response = Loan.delete(loan_id)
        return response


class LoansBySampleResource(Resource):

    @marshal_with(Loan.simple_fields())
    def get(self, sample_id):
        response = Loan.get_by_sample(sample_id)
        return response


class BookAuthorAsossiationResource(Resource):

    def post(self, book_id, author_id):
        response = Book.create_author_assoc(book_id, author_id)
        return response

    def delete(self, book_id, author_id):
        response = Book.delete_author_assoc(book_id, author_id)
        return response



extensions.api.add_resource(PingResource, '/ping')
extensions.api.add_resource(AuthorResource, '/authors')
extensions.api.add_resource(AuthorResourceWithId, '/authors/<string:author_id>')
extensions.api.add_resource(BookResource, '/books')
extensions.api.add_resource(BookResourceWithId, '/books/<string:book_id>')

extensions.api.add_resource(BookAuthorAsossiationResource, '/books/<string:book_id>/authors/<string:author_id>')

extensions.api.add_resource(SampleResource, '/samples')
extensions.api.add_resource(SampleResourceWithId, '/samples/<string:sample_id>')
extensions.api.add_resource(MemberResource, '/members')
extensions.api.add_resource(MemberResourceWithId, '/members/<string:member_id>')
extensions.api.add_resource(LoanResource, '/loans')
extensions.api.add_resource(LoanResourceWithId, '/loans/<string:loan_id>')
extensions.api.add_resource(LoansBySampleResource, '/samples/<string:sample_id>/loans')




