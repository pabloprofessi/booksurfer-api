import json
from flask_restful import Resource, marshal_with
from flask import request

from . import extensions

from models import Author
from models import Book
from models import Sample
from models import Member
from models import Loan

import datetime


def simple_response(response, entity_class):
    if type(response) is entity_class:
        @marshal_with(entity_class.simple_fields())
        def good_response(response):return response
        return good_response(response)
    else:
        return response[0], response[1]

def complete_response(response, entity_class):
    if type(response) is entity_class:
        @marshal_with(entity_class.complete_fields())
        def good_response(response):return response
        return good_response(response)
    else:
        return response[0], response[1]


class PingResource(Resource):
    def get(self):
        return "pong"

class AuthorResource(Resource):

    def get(self):
        response = Author.query.all()
        return complete_response(response, Author)

    def post(self):
        json_data = request.get_json(force=True)
        response = Author.create(
            json_data['firstName'], 
            json_data['lastName'], 
            json_data['nationality'])
        return simple_response(response, Author)

class AuthorResourceWithId(Resource):

    def get(self, author_id):
        response = Author.get(author_id)
        return complete_response(response, Author)

    def put(self, author_id):
        json_data = request.get_json(force=True)
        response = Author.update(author_id,
            json_data['firstName'], 
            json_data['lastName'], 
            json_data['nationality'])
        return simple_response(response, Author)

    def delete(self, author_id):
        response = Author.delete(author_id)
        return simple_response(response, Author)

class BookResource(Resource):

    def get(self):
        response = Book.get_all()
        return complete_response(response, Book)

    def post(self):
        json_data = request.get_json(force=True)
        response = Book.create(
            json_data['title'], 
            json_data['publisher'], 
            json_data['editionYear'], 
            json_data['editionCountry'], 
            json_data['price'],
            json_data['isbn'],
            json_data['gender'],
            json_data['reputationValue'],
            json_data['loanType'])
        return complete_response(response, Book)


class BookResourceWithId(Resource):

    def get(self, book_id):
        response = Book.get(book_id)
        return complete_response(response, Book)

    def put(self, book_id):
        json_data = request.get_json(force=True)
        response = Book.update(book_id,
            json_data['title'], 
            json_data['publisher'], 
            json_data['editionYear'], 
            json_data['editionCountry'], 
            json_data['price'],
            json_data['isbn'],
            json_data['gender'],
            json_data['reputationValue'],
            json_data['loanType'])
        return simple_response(response, Book)

    def delete(self, book_id):
        response = Book.delete(book_id)
        return simple_response(response, Book)


class SampleResource(Resource):

    def get(self):
        response = Sample.get_all()
        return complete_response(response, Sample)

    def post(self):
        json_data = request.get_json(force=True)
        response = Sample.create(
            json_data['bookId'],
            json_data['acquisitionDate'], 
            json_data.get('discardDate',None), 
            json_data['barCode'])
        return simple_response(response, Sample)
        

class SampleResourceWithId(Resource):

    def get(self, sample_id):
        response = Sample.get(sample_id)
        return simple_response(response, Sample)

    def put(self, sample_id):
        json_data = request.get_json(force=True)
        response = Sample.update(sample_id,
                json_data['acquisitionDate'], 
                json_data.get('discardDate',None),
                json_data['barCode'])
        return simple_response(response, Sample)

    def delete(self, sample_id):
        response = Sample.delete(sample_id)
        return simple_response(response, Sample)


class MemberResource(Resource):

    def get(self):
        response = Member.get_all()
        return simple_response(response, Member)

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
        return simple_response(response, Member)

class MemberResourceWithId(Resource):

    def get(self, member_id):
        response = Member.get(member_id)
        return simple_response(response, Member)

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
        return simple_response(response, Member)

    def delete(self, member_id):
        response = Member.delete(member_id)
        return simple_response(response, Member)



class LoanResource(Resource):

    def get(self):
        response = Loan.query.all()
        return simple_response(response, Loan)

    def post(self):
        json_data = request.get_json(force=True)
        response = Loan.create(
            json_data['memberId'],
            json_data['sampleId'],
            json_data['withdrawDate'],
            json_data['comment'],
            json_data['loanType'])
        return simple_response(response, Loan)

class LoanResourceWithId(Resource):

    def get(self, loan_id):
        response = Loan.get(loan_id)
        return simple_response(response, Loan)

    def put(self, loan_id):
        json_data = request.get_json(force=True)
        response = Loan.update(loan_id,
            json_data.get(['returnDate'], str(datetime.datetime.now().date())),
            json_data['comment'])
        return simple_response(response, Loan)

    def delete(self, loan_id):
        response = Loan.delete(loan_id)
        return simple_response(response, Loan)


class LoansBySampleResource(Resource):

    def get(self, sample_id):
        response = Loan.get_by_sample(sample_id)
        return simple_response(response, Loan)


class BookAuthorAsossiationResource(Resource):

    def post(self, book_id, author_id):
        response = Book.create_author_assoc(book_id, author_id)
        return response

    def delete(self, book_id, author_id):
        response = Book.delete_author_assoc(book_id, author_id)
        return response

class LoansByMemberResource(Resource):

    def get(self, member_id):
        response = Loan.get_loans_by_member(member_id)
        return simple_response(response, Loan)



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

extensions.api.add_resource(LoansByMemberResource, '/members/<string:member_id>/loans')


