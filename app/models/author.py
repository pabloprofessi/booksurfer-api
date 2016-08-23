from ..extensions import db
from flask_restful import fields


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    image_url = db.Column(db.String(200))
    nationality = db.Column(db.String(50))


    @staticmethod
    def simple_fields():
        return {
                'id': fields.String,
                'first_name': fields.String,
                'last_name': fields.String,
                'image_url': fields.String,
                'nationality': fields.String,
                }
    

