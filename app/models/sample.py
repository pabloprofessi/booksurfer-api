from ..extensions import db
from flask_restful import fields
import datetime

def string_to_date(a_date):
    if a_date:
        a_date = datetime.datetime.strptime(a_date, '%Y-%m-%d').date()
    return a_date

class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loans = db.relationship('Loan', backref='sample', lazy='select', uselist=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'),nullable=False)
    acquisition_date =db.Column(db.Date)
    discard_date = db.Column(db.Date)
    bar_code = db.Column(db.String(32))
    erased = db.Column(db.Boolean, default=False)

    @staticmethod
    def complete_fields():
        from book import Book
        return {
                'id': fields.String,
                'book':  fields.Nested(Book.simple_fields()),
                'acquisitionDate': fields.String(attribute='acquisition_date'),
                'discardDate': fields.String(attribute='discard_date'),
                'barCode': fields.String(attribute='bar_code'),
                'availableForLoan': fields.String(attribute='available_for_loan'),
                }

    @staticmethod
    def simple_fields():
        return {
                'id': fields.String,
                'bookId': fields.String(attribute='book_id'),
                'acquisitionDate': fields.String(attribute='acquisition_date'),
                'discardDate': fields.String(attribute='discard_date'),
                'barCode': fields.String(attribute='bar_code'),
                'availableForLoan': fields.String(attribute='available_for_loan'),
                }

    @staticmethod
    def get(id):
        return Sample.query.get(id)


    @staticmethod
    def get_all():
        return Sample.query.filter_by(erased=False).all()

    @staticmethod
    def get_active_by_book(book_id):
        return Sample.query.filter_by(book_id=book_id, erased=False).all()

        


    
    @staticmethod
    def create(book_id, acquisition_date, discard_date, bar_code):
        acquisition_date = string_to_date(acquisition_date)
        discard_date = string_to_date(discard_date)
        has_one = Sample.query.filter_by(book_id=book_id, bar_code=bar_code).first()
        if has_one:
            return {'message' : 'Ya tienes un ejemplar con ese codigo de barra!'}, 400    
        new_sample = Sample(book_id=book_id, acquisition_date=acquisition_date, discard_date=discard_date, bar_code=bar_code)
        db.session.add(new_sample)
        db.session.commit()
        return new_sample

    #@staticmethod
    #def create_with_book(acquisition_date, discard_date, bar_code):
    #    acquisition_date = string_to_date(acquisition_date)
    #    discard_date = string_to_date(discard_date)
    #    has_one = Sample.query.filter_by(bar_code=bar_code).first()
    #    if has_one:
    #        has_one.message = ('Ya tienes un ejemplar con ese codigo de barra!', 400)
    #        return has_one
    #    new_sample = Sample(acquisition_date=acquisition_date, discard_date=discard_date, bar_code=bar_code)
    #    return new_sample

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
            if (sample.is_loaned) and (sample.erased == False): 
                return {'message' : 'El ejemplar no puede ser borado, ha sido prestado.'}, 400
            sample.erased = True
            db.session.commit()
        return sample

    @property
    def available_for_loan(self):
        from loan import Loan
        if self.discard_date or self.is_loaned:
            return False
        return True

    @property
    def loans_count(self):
        loans_list = self.loans
        db.session.commit()
        return len(loans_list)


    @property
    def is_loaned(self):
        from loan import Loan
        loan_list = self.loans
        db.session.commit()
        for sample_loan in loan_list:
            if (sample_loan.return_date == None) : 
                return True
        return False
        