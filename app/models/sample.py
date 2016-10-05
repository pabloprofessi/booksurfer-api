from ..extensions import db
from flask_restful import fields



class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loans = db.relationship('Loan', backref='sample', lazy='dynamic', uselist=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'),nullable=False)
    acquisition_date =db.Column(db.DateTime)
    discard_date = db.Column(db.DateTime)
    bar_code = db.Column(db.String(32))

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
        has_one = Sample.query.filter_by(book_id=book_id, acquisition_date=acquisition_date, bar_code=bar_code).first()
        if has_one:
            return has_one    
        new_sample = Sample(book_id=book_id, acquisition_date=acquisition_date, discard_date=discard_date, bar_code=bar_code)
        db.session.add(new_sample)
        db.session.commit()
        return new_sample

    @staticmethod
    def update(id, book_id, acquisition_date, discard_date, bar_code):
        sample = Sample.query.get(id)
        if sample:
            sample.book_id = book_id 
            sample.acquisition_date = acquisition_date 
            sample.discard_date = discard_date 
            sample.bar_code = bar_code 
        db.session.commit()
        return sample

    @staticmethod
    def delete(id):
        sample = Sample.query.get(id)
        if book:
            db.session.delete(sample)
            db.session.commit()
        return sample
