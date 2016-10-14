from ..extensions import db
from flask_restful import fields

from loan import Loan

def str_to_bool(a_string):
    return a_string.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']
    
    


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loans = db.relationship('Loan', backref='member', lazy='dynamic', uselist=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    dni = db.Column(db.String(16))
    nationality = db.Column(db.String(50))
    cuil = db.Column(db.String(24))
    phone = db.Column(db.String(24))
    email = db.Column(db.String(100))
    zip_code = db.Column(db.String(10))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    enabled = db.Column(db.Boolean, default=True)
    reputation = db.Column(db.Integer)


    @staticmethod
    def simple_fields():
        return {
            'id' : fields.String,
            'firstName' : fields.String(attribute='first_name'),
            'lastName' : fields.String(attribute='last_name'),
            'dni' : fields.String,
            'nationality' : fields.String,
            'cuil' : fields.String,
            'phone' : fields.String,
            'email' : fields.String,
            'zipCode' : fields.String(attribute='zip_code'),
            'city' : fields.String,
            'state' : fields.String,
            'enabled' : fields.String,
            'reputation' : fields.String,
        }

    @staticmethod
    def complete_fields():
        return {
            'id' : fields.String,
            'firstName' : fields.String(attribute='first_name'),
            'lastName' : fields.String(attribute='last_name'),
            'dni' : fields.String,
            'nationality' : fields.String,
            'cuil' : fields.String,
            'phone' : fields.String,
            'email' : fields.String,
            'zipCode' : fields.String(attribute='zip_code'),
            'city' : fields.String,
            'state' : fields.String,
            'enabled' : fields.String,
            'reputation' : fields.String,
            'loans': fields.List(fields.Nested(Loans.simple_fields()), attribute='loans'),
        }


    @staticmethod
    def get(id):
        return Member.query.get(id);


    @staticmethod
    def create(first_name, last_name, dni, nationality, cuil, phone, email, zip_code, city, state, enabled, reputation):
        has_one = Member.query.filter_by(first_name=first_name, last_name=last_name, dni=dni).first()
        if has_one:
            return has_one
        new_one = Member(first_name=first_name, last_name=last_name, dni=dni, nationality=nationality, 
                        cuil=cuil, phone=phone, email=email, zip_code=zip_code, city=city, state=state, 
                        enabled=str_to_bool(enabled), reputation=reputation)
        db.session.add(new_one)
        db.session.commit()
        return new_one

    @staticmethod
    def update(id, first_name, last_name, dni, nationality, cuil, phone, email, zip_code, city, state, enabled, reputation):
        member = Member.query.get(id)
        if member:
            member.first_name = first_name
            member.last_name = last_name
            member.dni = dni
            member.nationality = nationality
            member.cuil = cuil
            member.phone = phone
            member.email = email
            member.zip_code = zip_code
            member.city = city
            member.state = state
            member.enabled = str_to_bool(enabled)
            member.reputation = reputation
        db.session.commit()
        return member

    @staticmethod
    def delete(id):
        member = Member.query.get(id)
        if member:
            db.session.delete(member)
            db.session.commit()
        return member



