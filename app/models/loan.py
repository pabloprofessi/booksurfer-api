from ..extensions import db
from flask_restful import fields
import datetime

def string_to_date(a_date):
    if a_date:
        a_date = datetime.datetime.strptime(a_date, '%Y-%m-%d').date()
    return a_date


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'),nullable=False)
    sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'),nullable=False)
    agreed_return_date = db.Column(db.Date)
    return_date = db.Column(db.Date)
    withdraw_date = db.Column(db.Date)
    comment = db.Column(db.Text)


    @staticmethod
    def simple_fields():
        return {
        'id' : fields.String,
        'memberId' : fields.String(attribute='member_id'),
        'sampleId' : fields.String(attribute='sample_id'),
        'agreedReturnDate' : fields.String(attribute='agreed_return_date'),
        'returnDate' : fields.String(attribute='return_date'),
        'withdrawDate' : fields.String(attribute='withdraw_date'),
        'comment' : fields.String,
        }

    @staticmethod
    def get(id):
        return Loan.query.get(id);

    @staticmethod
    def create(member_id, sample_id, agreed_return_date, return_date, withdraw_date, comment):
        agreed_return_date = string_to_date(agreed_return_date)
        return_date = string_to_date(return_date)
        withdraw_date = string_to_date(withdraw_date)
        has_one = Loan.query.filter_by(member_id=member_id, sample_id=sample_id).first()
        if has_one:
            return has_one
        new_one = Loan(member_id=member_id,sample_id=sample_id,agreed_return_date=agreed_return_date,return_date=return_date,withdraw_date=withdraw_date,comment=comment)
        db.session.add(new_one)
        db.session.commit()
        return new_one

    @staticmethod
    def update(id, member_id, sample_id, agreed_return_date, return_date, withdraw_date, comment):
        loan = Loan.query.get(id)
        agreed_return_date = string_to_date(agreed_return_date)
        return_date = string_to_date(return_date)
        withdraw_date = string_to_date(withdraw_date)
        if loan:
            loan.member_id = member_id
            loan.sample_id = sample_id
            loan.agreed_return_date = agreed_return_date
            loan.return_date = return_date
            loan.withdraw_date = withdraw_date
            loan.comment = comment            
        db.session.commit()
        return loan

    @staticmethod
    def delete(id):
        loan = Loan.query.get(id)
        if loan:
            db.session.delete(loan)
            db.session.commit()
        return loan



