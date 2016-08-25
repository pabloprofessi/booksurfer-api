from ..extensions import db
from flask_restful import fields


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    publisher = db.Column(db.String(200))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    image_url = db.Column(db.String(500))
    publish_year = db.Column(db.String(4))
    editorial = db.Column(db.String(200))
    copies_available = db.Column(db.Integer)
    copies_total = db.Column(db.Integer)

    @staticmethod
    def simple_fields():
        return {
                'id': fields.String,
                'title': fields.String,
                'publisher': fields.String,
                'author_id': fields.String,
                'image_url': fields.String,
                'publish_year': fields.String,
                'editorial': fields.String,
                'copies_available': fields.String,
                'copies_total': fields.String
                }

    @staticmethod
    def get(id):
        return Book.query.get(id);
    
    @staticmethod
    def create(title, publisher, author_id, image_url, publish_year, editorial):
        has_one = Book.query.filter_by(title=title, publisher=publisher, publish_year=publish_year, editorial=editorial).first()
        if has_one:
            return has_one
        new_one = Book(title=title, publisher=publisher, author_id=author_id, image_url=image_url, publish_year=publish_year, editorial=editorial, copies_available=0, copies_total=0)
        db.session.add(new_one)
        db.session.commit()
        return new_one

    @staticmethod
    def update(id, publisher, author_id, image_url, publish_year, editorial, copies_available, copies_total):
        book = Book.query.get(id)
        if book:
            book.title = title 
            book.publisher = publisher 
            book.author_id = author_id 
            book.image_url = image_url 
            book.publish_year = publish_year 
            book.editorial = editorial 
            book.copies_available = copies_available 
            book.copies_total = copies_total 
        db.session.commit()
        return author

    @staticmethod
    def delete(id):
        book = Book.query.get(id)
        if book:
            db.session.delete(book)
            db.session.commit()
        return book
