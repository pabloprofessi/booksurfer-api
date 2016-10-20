from ..extensions import db
from flask_restful import fields
import datetime
import loan_logic

def string_to_date(a_date):
    if a_date:
        return datetime.datetime.strptime(a_date, '%Y-%m-%d').date()


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'),nullable=False)
    sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'),nullable=False)
    agreed_return_date = db.Column(db.Date)
    return_date = db.Column(db.Date)
    withdraw_date = db.Column(db.Date)
    comment = db.Column(db.Text)
    #valores posibles por ahora LOCAL o REMOTE
    loan_type = db.Column(db.String(10))


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
        'loanType': fields.String(attribute='loan_type'),
        }

    @staticmethod
    def get(id):
        return Loan.query.get(id)

    @staticmethod
    def get_pending_loans_by_member(member_id):
        return Loan.query.filter_by(member_id=member_id, return_date=None).all()
    
    @staticmethod
    def get_loans_by_member(member_id):
        return Loan.query.filter_by(member_id=member_id).all()

    @staticmethod
    def get_by_sample(sample_id):
        return Loan.query.filter_by(sample_id=sample_id).all()

    @staticmethod
    def get_pending_loan_by_sample(sample_id):
        return Loan.query.filter_by(sample_id=sample_id, return_date=None).first()

    @staticmethod
    def create(member_id, sample_id, withdraw_date, comment, loan_type):
        if loan_logic.loan_is_allowed_for_member(member_id, sample_id):
            withdraw_date = string_to_date(withdraw_date)
            agreed_return_date =  loan_logic.get_agreed_return_date(withdraw_date)
            has_one = Loan.query.filter_by(member_id=member_id, sample_id=sample_id).first()
            if has_one:
                return has_one
            new_one = Loan(member_id=member_id,sample_id=sample_id,agreed_return_date=agreed_return_date,return_date=return_date,withdraw_date=withdraw_date,comment=comment, loan_type=loan_type)
            db.session.add(new_one)
            db.session.commit()
        else:
            return 'El socio no esta hablitado para tener prestamos.', 400
        return new_one

    @staticmethod
    def update(id, return_date, comment):
        loan = Loan.get(id)
        if loan:
            agreed_return_date = string_to_date(agreed_return_date)
            return_date = string_to_date(return_date)
            loan.agreed_return_date = agreed_return_date
            loan.return_date = return_date
            loan.comment = comment   
            if loan.loan_type == 'REMOTE':
                loan_logic.get_updated_member_reputation(loan.member_id)         
            db.session.commit()
        return loan

    @staticmethod
    def delete(id):
        loan = Loan.query.get(id)
        if loan:
            db.session.delete(loan)
            db.session.commit()
        return loan


