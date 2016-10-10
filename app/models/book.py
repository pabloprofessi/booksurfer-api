from ..extensions import db
from flask_restful import fields

from author import Author
from sample import Sample

books_author = db.Table('books_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), nullable=False),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'),nullable=False),
    db.PrimaryKeyConstraint('book_id', 'author_id')
)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    authors = db.relationship('Author', secondary=books_author,
        backref=db.backref('books', lazy='dynamic'))
    samples = db.relationship('Sample', backref='book', lazy='dynamic', uselist=True)
    title = db.Column(db.String(200))
    publisher = db.Column(db.String(200))
    edition_year = db.Column(db.String(4))
    edition_country = db.Column(db.String(64))
    price = db.Column(db.String(10))
    isbn = db.Column(db.String(10))
    reputation_value = db.Column(db.Integer)

    

    @staticmethod
    def simple_fields():
        return {
                'id': fields.String,
                'title': fields.String,
                'publisher': fields.String,
                'editionYear': fields.String(attribute='edition_year'),
                'editionCountry': fields.String(attribute='edition_country'),
                'price': fields.String,
                'isbn': fields.String,
                'reputationValue': fields.String(attribute='reputation_value'),
                }


    @staticmethod
    def complete_fields():
        return {
                'id': fields.String,
                'title': fields.String,
                'publisher': fields.String,
                'editionYear': fields.String(attribute='edition_year'),
                'editionCountry': fields.String(attribute='edition_country'),
                'price': fields.String,
                'isbn': fields.String,
                'reputationValue': fields.String(attribute='reputation_value'),
                'authors': fields.List(fields.Nested(Author.simple_fields()), attribute='authors'),
                'samples': fields.List(fields.Nested(Sample.simple_fields()), attribute='samples'),
                }

    @staticmethod
    def get(id):
        return Book.query.get(id);
    
    @staticmethod
    def create(title, publisher, edition_year, edition_country, price, isbn, reputation_value, samples, authors):
        has_one = Book.query.filter_by(isbn=isbn).first()
        if has_one:
            return has_one    
        new_book = Book(title=title, publisher=publisher,  edition_year=edition_year, edition_country=edition_country, price=price, isbn=isbn, reputation_value=reputation_value)   
        for a_author in authors:
            new_author = Author.create_with_book(a_author['firstName'], a_author['lastName'],  a_author['nationality'])
            new_book.authors.append(new_author)
        for a_sample in samples:
            new_sample = Sample.create_with_book(a_sample.get('acquisitionDate'), a_sample.get('discardDate',None), a_sample['barCode'])
            new_book.samples.append(new_sample)
        db.session.add(new_book)
        db.session.commit()
        return new_book

    @staticmethod
    def update(id, title, publisher, edition_year, edition_country, price, isbn, reputation_value):
        book = Book.query.get(id)
        if book:
            book.title = title 
            book.publisher = publisher 
            book.edition_year = edition_year 
            book.edition_country = edition_country
            book.price = price
            book.isbn = isbn
            book.reputation_value = reputation_value
        db.session.commit()
        return book

    @staticmethod
    def delete(id):
        book = Book.query.get(id)
        if book:
            for sample in book.samples:
                db.session.delete(sample)
            for author in book.authors:
                db.session.delete(author)
            db.session.delete(book)
            db.session.commit()
        return book
