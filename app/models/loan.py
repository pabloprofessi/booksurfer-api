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
    def complete_fields():
        from sample import Sample
        return {
        'id' : fields.String,
        'memberId' : fields.String(attribute='member_id'),
        'sample' : fields.Nested(Sample.complete_fields()),
        'agreedReturnDate' : fields.String(attribute='agreed_return_date'),
        'returnDate' : fields.String(attribute='return_date'),
        'withdrawDate' : fields.String(attribute='withdraw_date'),
        'comment' : fields.String,
        'loanType': fields.String(attribute='loan_type'),
        }

    @staticmethod
    def for_report_fields():
        from sample import Sample
        from member import Member
        return {
        'id' : fields.String,
        'member' : fields.Nested(Member.minimal_fields()),
        'sample' : fields.Nested(Sample.complete_fields()),
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
    def get_latest_loans():
        oldest_date = datetime.datetime.now().date() - datetime.timedelta(days=365)
        return Loan.query.filter(Loan.withdraw_date >= oldest_date).all()

    @staticmethod
    def get_pending_loans(member_id):
        now_date = datetime.datetime.now().date()
        return Loan.query.filter(Loan.return_date == None, Loan.agreed_return_date > now_date).all()

    @staticmethod
    def get_pending_loans_by_member(member_id):
        return Loan.query.filter_by(member_id=member_id, return_date=None).all()
    
    @staticmethod
    def get_loans_by_member(member_id):
        return Loan.query.filter_by(member_id=member_id).order_by('withdraw_date desc').all()

    @staticmethod
    def get_by_sample(sample_id):
        return Loan.query.filter_by(sample_id=sample_id).all()

    @staticmethod
    def get_pending_loan_by_sample(sample_id):
        return Loan.query.filter_by(sample_id=sample_id, return_date=None).first()

    @staticmethod
    def create(member_id, sample_id, withdraw_date, loan_type):
        is_allowd_and_reason = loan_logic.loan_is_allowed_for_member(member_id, sample_id)
        if is_allowd_and_reason[0]:
            withdraw_date = string_to_date(withdraw_date)

            agreed_return_date =  loan_logic.get_agreed_return_date(withdraw_date,loan_type)
            has_one = Loan.query.filter_by(member_id=member_id, 
                                           sample_id=sample_id,
                                           withdraw_date=withdraw_date,
                                           return_date=None).first()
            if has_one:
                return {'message' : 'El prestamo ya fue creado.'}, 400
            new_one = Loan(member_id=member_id,
                           sample_id=sample_id,
                           agreed_return_date=agreed_return_date,
                           withdraw_date=withdraw_date,
                           loan_type=loan_type)
            db.session.add(new_one)
            db.session.commit()
        else:
            return {'message' : is_allowd_and_reason[1]}, 400
        return new_one

    @staticmethod
    def update(id, return_date, comment):
        from member import Member
        loan = Loan.get(id)
        if loan:
            loan.return_date = string_to_date(return_date)
            loan.comment = comment   
            loan_logic.get_updated_member_reputation(Member.get(loan.member_id))         
            db.session.commit()
        return loan

    @staticmethod
    def delete(id):
        loan = Loan.query.get(id)
        if loan:
            db.session.delete(loan)
            db.session.commit()
        return loan


