from ..extensions import db
from flask_restful import fields


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    image_url = db.Column(db.String(500))
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

    @staticmethod
    def get(id):
        return Author.query.get(id);
    
    @staticmethod
    def create(first_name, last_name, image_url, nationality):
        has_one = Author.query.filter_by(first_name=first_name, last_name=last_name,nationality=nationality).first()
        if has_one:
            return has_one
        new_one = Author(first_name=first_name, last_name=last_name, image_url=image_url,  nationality=nationality)
        db.session.add(new_one)
        db.session.commit()
        return new_one

    @staticmethod
    def update(id, first_name, last_name, image_url, nationality):
        author = Author.query.get(id)
        if author:
            author.first_name = first_name
            author.last_name = last_name
            author.image_url = image_url
            author.nationality = nationality
        db.session.commit()
        return author

    @staticmethod
    def delete(id):
        author = Author.query.get(id)
        if author:
            db.session.delete(author)
            db.session.commit()
        return author



