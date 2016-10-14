from ..extensions import db
from flask_restful import fields
import datetime

   

def string_to_date(a_date):
    if a_date:
        a_date = datetime.datetime.strptime(a_date, '%Y-%m-%d').date()
    return a_date

class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loans = db.relationship('Loan', backref='sample', lazy='dynamic', uselist=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'),nullable=False)
    acquisition_date =db.Column(db.Date)
    discard_date = db.Column(db.Date)
    bar_code = db.Column(db.String(32))

    @staticmethod
    def complete_fields():
        from book import Book
        return {
                'id': fields.String,
                'book':  fields.Nested(Book.simple_fields()),
                'acquisitionDate': fields.String(attribute='acquisition_date'),
                'discardDate': fields.String(attribute='discard_date'),
                'barCode': fields.String(attribute='bar_code'),
                }

    @staticmethod
    def simple_fields():
        return {
                'id': fields.String,
                'bookId': fields.String(attribute='book_id'),
                'acquisitionDate': fields.String(attribute='acquisition_date'),
                'discardDate': fields.String(attribute='discard_date'),
                'barCode': fields.String(attribute='bar_code'),
                }

    @staticmethod
    def get(id):
        return Sample.query.get(id)
    
    @staticmethod
    def create(book_id, acquisition_date, discard_date, bar_code):
        acquisition_date = string_to_date(acquisition_date)
        discard_date = string_to_date(discard_date)
        has_one = Sample.query.filter_by(book_id=book_id, acquisition_date=acquisition_date, bar_code=bar_code).first()
        if has_one:
            return has_one    
        new_sample = Sample(book_id=book_id, acquisition_date=acquisition_date, discard_date=discard_date, bar_code=bar_code)
        db.session.add(new_sample)
        db.session.commit()
        return new_sample

    @staticmethod
    def create_with_book(acquisition_date, discard_date, bar_code):
        acquisition_date = string_to_date(acquisition_date)
        discard_date = string_to_date(discard_date)
        has_one = Sample.query.filter_by(acquisition_date=acquisition_date, bar_code=bar_code).first()
        if has_one:
            return has_one    
        new_sample = Sample(acquisition_date=acquisition_date, discard_date=discard_date, bar_code=bar_code)
        return new_sample

    @staticmethod
    def update(id, acquisition_date, discard_date, bar_code):
        sample = Sample.query.get(id)
        if acquisition_date:
            acquisition_date = datetime.datetime.strptime(acquisition_date, '%Y-%m-%d').date()
        if discard_date:
            discard_date = datetime.datetime.strptime(discard_date, '%Y-%m-%d').date() 
        if sample:
            sample.acquisition_date = acquisition_date 
            sample.discard_date = discard_date 
            sample.bar_code = bar_code 
        db.session.commit()
        return sample

    @staticmethod
    def delete(id):
        sample = Sample.query.get(id)
        if sample:
            db.session.delete(sample)
            db.session.commit()
        return sample
