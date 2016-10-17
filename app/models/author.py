from ..extensions import db
from flask_restful import fields


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    nationality = db.Column(db.String(50))
    
    @staticmethod
    def simple_fields():
        return {
                'id': fields.String,
                'firstName': fields.String(attribute='first_name'),
                'lastName': fields.String(attribute='last_name'),
                'nationality': fields.String,
                }

    @staticmethod            
    def complete_fields():
        from book import Book
        return {
                'id': fields.String,
                'firstName': fields.String(attribute='first_name'),
                'lastName': fields.String(attribute='last_name'),
                'nationality': fields.String,
                'books': fields.List(fields.Nested(Book.simple_fields()), attribute='books'),
                }


    @staticmethod
    def get(id):
        return Author.query.get(id);
    
    @staticmethod
    def create(first_name, last_name, nationality):
        has_one = Author.query.filter_by(first_name=first_name, last_name=last_name,nationality=nationality).first()
        if has_one:
            return has_one
        new_one = Author(first_name=first_name, last_name=last_name,  nationality=nationality)
        db.session.add(new_one)
        db.session.commit()
        return new_one


    @staticmethod
    def update(id, first_name, last_name, nationality):
        author = Author.query.get(id)
        if author:
            author.first_name = first_name
            author.last_name = last_name
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



