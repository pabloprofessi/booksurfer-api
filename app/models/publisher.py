from ..extensions import db
from flask_restful import fields


class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    @staticmethod
    def simple_fields():
        return {
                'id': fields.String,
                'name': fields.String
                }


    @staticmethod
    def get(id):
        return Publisher.query.get(id);
    
    @staticmethod 
    def create(name):
        has_one = Publisher.query.filter_by(name=name).first()
        if has_one:
            return has_one
        new_one = Publisher(name=name)
        db.session.add(new_one)
        db.session.commit()
        return new_one


    @staticmethod
    def update(id, name):
        publisher = Publisher.query.get(id)
        if publisher:
            publisher.name = name
        db.session.commit()
        return publisher

    @staticmethod
    def delete(id):
        publisher = Publisher.query.get(id)
        if publisher:
            db.session.delete(publisher)
            db.session.commit()
        return publisher






