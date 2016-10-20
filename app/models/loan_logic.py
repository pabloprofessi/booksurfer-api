from ..extensions import db


from sample import Sample
from book import Book
from datetime import datetime
from datetime import date
from datetime import timedelta

GOOD_TERM_REPUTATION_CONSTANT = 0.1
BAD_TERM_REPUTATION_CONSTANT = 0.3
DAYS_TO_RETURN_BOOK = 12


def loan_is_allowed_for_member(member_id, sample_id):
    from member import Member
    a_member = Member.get(member_id)
    get_updated_member_reputation(a_member)
    a_sample = Sample.get(sample_id)
    a_book = Book.get(a_sample.book_id)

    if (not a_book.erased) and (not a_sample.erased) and (not a_member.erased):
        return False, "Libro ejemplar o socio han sido borrados."
    if a_sample.discard_date:
        return False, "El ejemplar ha sido descartado."
    if not member_is_enabled(a_member):
        return False, "El socio no esta habilitado para recibir prestamos."
    if not book_is_loanable(a_book):
        return False,  "El libro no esta habilitado para prestamos remotos."
    if not allowed_by_book_puntuation(a_member, a_book):
        return False,  "La reputacion del libro es demasiado alta para ser prestado a ese socio."
    if debt_more_than_three_books(member_id):
        update_member_to_loan(a_member, False)
        return False, "El socio ya tiene mas de 3 libros prestados."
    if member_is_suspended(member_id):
        update_member_to_loan(a_member, False)
        return False, "El socio esta suspendido hasta: " + str(get_suspention_end_date(a_member)) + "."
    update_member_to_loan(a_member, True)
    return True

def member_is_enabled(a_member):
    return a_member.enabled


def book_is_loanable(a_book):
    return a_book.loan_type == 'REMOTE'

def allowed_by_book_puntuation(a_member, a_book):
    return a_member.reputation >= a_book.reputation

def debt_more_than_three_books(member_id):
    from loan import Loan
    pending_loan_list = Loan.get_pending_loans_by_member(member_id)
    return (len(pending_loan_list) >= 3)


def member_is_suspended(a_member):
    suspention_days = calc_end_suspention_days(a_member)   
    return suspention_days == 0

def update_member_to_loan(a_member, state):
    a_member.authorized_to_loan = state
    db.session.commit()
        

def get_suspention_end_date(a_member):
    days = calc_end_suspention_days(a_member)
    return datetime.now().date() + timedelta(days=days)


def calc_end_suspention_days(a_member):
    from loan import Loan
    pending_loan_list = Loan.get_pending_loans_by_member(a_member.id)
    pendind_suspension_days = 0
    for a_loan in pending_loan_list:
        time_difference = datetime.now().date() - a_loan.agreed_return_date 
        if time_difference.days < 0:
            pendind_suspension_days = 2 * (pendind_suspension_days + abs(time_difference.days))
    return pendind_suspension_days



def member_is_allowed(member_id):
    from member import Member
    a_member = Member.get(member_id)
    return a_member.enabled

def get_agreed_return_date(withdraw_date):
    return withdraw_date + timedelta(days=DAYS_TO_RETURN_BOOK)

# cada vez q se devuelve un libro!
def get_updated_member_reputation(a_member):
    from loan import Loan
    member_loan_list = Loan.get_loans_by_member(a_member.id)
    for member_loan in member_loan_list:
        datediff = member_loan.agreed_return_date - datetime.now().date()
        if datediff.days < 0:
            #si lo entrego fuera de fecha resta
            a_member.reputation = a_member.reputation + (BAD_TERM_REPUTATION_CONSTANT * datediff.days)
        else:
            #si lo entrego en fecha suma
            a_member.reputation = a_member.reputation + (GOOD_TERM_REPUTATION_CONSTANT)
        if a_member.reputation > 10 : a_member.reputation = 10
        if a_member.reputation <= 0 : a_member.reputation = 0
    
    db.session.commit()

    