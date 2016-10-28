from ..extensions import db
from flask_restful import fields


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role = db.Column(db.String(10))
    dni = db.Column(db.String(10))

    @staticmethod
    def simple_fields():
        return {
                'id': fields.String,
                'username': fields.String,
                'firstName': fields.String(attribute='first_name'),
                'lastName': fields.String(attribute='last_name'),
                'password': fields.String,
                'role': fields.String,
                'dni': fields.String
                }


    @staticmethod
    def get(id):
        return User.query.get(id);
    
    @staticmethod 
    def create(username, first_name, last_name, password, role, dni):
        has_one = User.query.filter_by(username=username).first()
        if has_one:
            return has_one
        new_one = User(username=username ,first_name=first_name ,last_name=last_name, password=password, role=role, dni=dni)
        db.session.add(new_one)
        db.session.commit()
        return new_one


    @staticmethod
    def update(id, username, first_name, last_name, password, role, dni):
        user = User.query.get(id)
        if user:
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.password  = password
            user.role = role
            user.dni = dni
        db.session.commit()
        return user

    @staticmethod
    def delete(id):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user






