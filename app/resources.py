import json
from flask_restful import Resource, marshal_with, marshal
from flask import request

from . import extensions

from models import Author
from models import Book
from models import Sample
from models import Member
from models import Loan
from models import User
from models import Publisher

from pprint import pprint
import datetime



class PingResource(Resource):
    def get(self):
        return "pong"


class PublishersResource(Resource):

    def get(self):
        response = Publisher.query.all()
        if len(response) > 0:
            if type(response[0]) is Publisher: 
                return marshal(response, Publisher.simple_fields())
        return response

    def post(self):
        json_data = request.get_json(force=True)
        response = Publisher.create(
            json_data['name'])
        if type(response) is Publisher: 
            return marshal(response, Publisher.simple_fields())
        return response

class PublishersResourceWithId(Resource):

    def get(self, publisher_id):
        response = Publisher.get(publisher_id)
        if type(response) is Publisher: 
            return marshal(response, Publisher.simple_fields())
        return response

    def put(self, publisher_id):
        json_data = request.get_json(force=True)
        response = Publisher.update(publisher_id,
            json_data['name'])
        if type(response) is Publisher: 
            return marshal(response, Publisher.simple_fields())
        return response

    def delete(self, publisher_id):
        response = Publisher.delete(publisher_id)
        if type(response) is Publisher: 
            return marshal(response, Publisher.simple_fields())
        return response





class UsersResource(Resource):

    def get(self):
        response = User.query.all()
        if len(response) > 0:
            if type(response[0]) is User: 
                return marshal(response, User.simple_fields())
        return response

    def post(self):
        json_data = request.get_json(force=True)
        response = User.create(
            json_data['username'],
            json_data['firstName'], 
            json_data['lastName'], 
            json_data['password'],
            json_data['role'],
            json_data['dni'])
        if type(response) is User: 
            return marshal(response, User.simple_fields())
        return response

class UsersResourceWithId(Resource):

    def get(self, user_id):
        response = User.get(user_id)
        if type(response) is User: 
            return marshal(response, User.simple_fields())
        return response

    def put(self, user_id):
        json_data = request.get_json(force=True)
        response = User.update(user_id,
            json_data['username'],
            json_data['firstName'], 
            json_data['lastName'], 
            json_data['password'],
            json_data['role'],
            json_data['dni'])
        if type(response) is User: 
            return marshal(response, User.simple_fields())
        return response

    def delete(self, user_id):
        response = User.delete(user_id)
        if type(response) is User: 
            return marshal(response, User.simple_fields())
        return response

class AuthorResource(Resource):

    def get(self):
        response = Author.query.all()
        if len(response) > 0:
            if type(response[0]) is Author: 
                return marshal(response, Author.complete_fields())
        return response

    def post(self):
        json_data = request.get_json(force=True)
        response = Author.create(
            json_data['firstName'], 
            json_data['lastName'], 
            json_data['nationality'])
        if type(response) is Author: 
            return marshal(response, Author.complete_fields())
        return response

class AuthorResourceWithId(Resource):

    def get(self, author_id):
        response = Author.get(author_id)
        if type(response) is Author: 
            return marshal(response, Author.complete_fields())
        return response

    def put(self, author_id):
        json_data = request.get_json(force=True)
        response = Author.update(author_id,
            json_data['firstName'], 
            json_data['lastName'], 
            json_data['nationality'])
        if type(response) is Author: 
            return marshal(response, Author.simple_fields())
        return response

    def delete(self, author_id):
        response = Author.delete(author_id)
        if type(response) is Author: 
            return marshal(response, Author.simple_fields())
        return response


class BookResource(Resource):
    
    def get(self):
        response = Book.get_all()
        if len(response) > 0:
            if type(response[0]) is Book: 
                return marshal(response, Book.complete_fields())
        return response

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
        if type(response) is Book: 
            return marshal(response, Book.complete_fields())
        return response


class BookResourceWithId(Resource):

    def get(self, book_id):
        response = Book.get(book_id)
        if type(response) is Book: 
            return marshal(response, Book.complete_fields())
        return response

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
        if type(response) is Book: 
            return marshal(response, Book.simple_fields())
        return response


    def delete(self, book_id):
        response = Book.delete(book_id)
        if type(response) is Book: 
            return marshal(response, Book.simple_fields())
        return response

class SampleResource(Resource):

    def get(self):
        response = Sample.get_all()
        if len(response) > 0:
            if type(response[0]) is Sample: 
                return marshal(response, Sample.complete_fields())
        return response

    def post(self):
        json_data = request.get_json(force=True)
        response = Sample.create(
            json_data['bookId'],
            json_data['acquisitionDate'], 
            json_data.get('discardDate',None), 
            json_data['barCode'])
        if type(response) is Sample: 
            return marshal(response, Sample.simple_fields())
        return response
        

class SampleResourceWithId(Resource):

    def get(self, sample_id):
        response = Sample.get(sample_id)
        if type(response) is Sample: 
            return marshal(response, Sample.complete_fields())
        return response

    def put(self, sample_id):
        json_data = request.get_json(force=True)
        response = Sample.update(sample_id,
                json_data['acquisitionDate'], 
                json_data.get('discardDate',None),
                json_data['barCode'])
        if type(response) is Sample: 
            return marshal(response, Sample.simple_fields())
        return response

    def delete(self, sample_id):
        response = Sample.delete(sample_id)
        if type(response) is Sample: 
            return marshal(response, Sample.simple_fields())
        return response

class MemberResource(Resource):
    
    def get(self):
        response = Member.get_all()
        if len(response) > 0:
            if type(response[0]) is Member: 
                return marshal(response, Member.simple_fields())
        return response

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
        if type(response) is Member: 
            return marshal(response, Member.simple_fields())
        return response


class MemberResourceWithId(Resource):

    def get(self, member_id):
        response = Member.get(member_id)
        if type(response) is Member: 
            return marshal(response, Member.simple_fields())
        return response



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
        if type(response) is Member: 
            return marshal(response, Member.simple_fields())
        return response


    def delete(self, member_id):
        response = Member.delete(member_id)
        if type(response) is Member: 
            return marshal(response, Member.simple_fields())
        return response


class LoanResource(Resource):

    def get(self):
        response = Loan.query.all()
        if len(response) > 0:
            if type(response[0]) is Loan: 
                return marshal(response, Loan.simple_fields())
        return response

    def post(self):
        json_data = request.get_json(force=True)
        response = Loan.create(
            json_data['memberId'],
            json_data['sampleId'],
            json_data['withdrawDate'],
            json_data['loanType'])
        if type(response) is Loan: 
            return marshal(response, Loan.simple_fields())
        return response

class LoanResourceWithId(Resource):

    def get(self, loan_id):
        response = Loan.get(loan_id)
        if type(response) is Loan: 
            return marshal(response, Loan.simple_fields())
        return response

    def put(self, loan_id):
        json_data = request.get_json(force=True)
        response = Loan.update(loan_id,
            json_data.get('returnDate', str(datetime.datetime.now().date())),
            json_data['comment'])
        if type(response) is Loan: 
            return marshal(response, Loan.simple_fields())
        return response

    def delete(self, loan_id):
        response = Loan.delete(loan_id)
        if type(response) is Loan: 
            return marshal(response, Loan.simple_fields())
        return response

class LoansBySampleResource(Resource):

    def get(self, sample_id):
        response = Loan.get_by_sample(sample_id)
        if len(response) > 0:
            if type(response[0]) is Loan: 
                return marshal(response, Loan.simple_fields())
        return response

class BookAuthorAsossiationResource(Resource):

    def post(self, book_id, author_id):
        response = Book.create_author_assoc(book_id, author_id)
        return response

    def delete(self, book_id, author_id):
        response = Book.delete_author_assoc(book_id, author_id)
        return response

class LoansByMemberResource(Resource):
    
    @marshal_with(Loan.complete_fields())
    def get(self, member_id):
        response = Loan.get_loans_by_member(member_id)
        return response

class LatestLoans(Resource):

    def get(self):
        response = Loan.get_latest_loans()
        if len(response) > 0:
            if type(response[0]) is Loan: 
                return marshal(response, Loan.for_report_fields())
        return response

class OutdatedLoans(Resource):

    def get(self):
        response = Loan.get_pending_loans()
        if len(response) > 0:
            if type(response[0]) is Loan: 
                return marshal(response, Loan.for_report_fields())
        return response


class PopularBooks(Resource):

    def get(self):
        response = Book.get_all_order_by_popularity()    
        if len(response) > 0:
            if type(response[0]) is Book: 
                book_list = marshal(response, Book.complete_fields())
                return book_list
        return response


extensions.api.add_resource(PingResource, '/ping')
extensions.api.add_resource(PublishersResource, '/publishers')
extensions.api.add_resource(PublishersResourceWithId, '/publishers/<string:publisher_id>')
extensions.api.add_resource(AuthorResource, '/authors')
extensions.api.add_resource(AuthorResourceWithId, '/authors/<string:author_id>')
extensions.api.add_resource(UsersResource, '/users')
extensions.api.add_resource(UsersResourceWithId, '/users/<string:user_id>')
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

extensions.api.add_resource(LatestLoans, '/reports/latest-loans')
extensions.api.add_resource(OutdatedLoans, '/reports/outdated-loans')
extensions.api.add_resource(PopularBooks, '/reports/popular-books')

