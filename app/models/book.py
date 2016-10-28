from ..extensions import db
from flask_restful import fields

from author import Author
from sample import Sample
from pprint import pprint

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
    edition_year = db.Column(db.Integer)
    edition_country = db.Column(db.String(64))
    price = db.Column(db.Float)
    isbn = db.Column(db.String(13))
    gender = db.Column(db.String(100))
    reputation_value = db.Column(db.Float)
    erased = db.Column(db.Boolean, default=False)
    #valores posibles por ahora LOCAL o REMOTE
    loan_type = db.Column(db.String(10))

    

    @staticmethod
    def simple_fields():
        return {
                'id': fields.String,
                'title': fields.String,
                'publisher': fields.String,
                'editionYear': fields.Integer(attribute='edition_year'),
                'editionCountry': fields.String(attribute='edition_country'),
                'price': fields.Float,
                'isbn': fields.String,
                'gender': fields.String,
                'reputationValue': fields.Float(attribute='reputation_value'),
                'loanType': fields.String(attribute='loan_type'),
                }


    @staticmethod
    def complete_fields():
        return {
                'id': fields.String,
                'title': fields.String,
                'publisher': fields.String,
                'editionYear': fields.Integer(attribute='edition_year'),
                'editionCountry': fields.String(attribute='edition_country'),
                'price': fields.Float,
                'isbn': fields.String,
                'gender': fields.String,
                'reputationValue': fields.Float(attribute='reputation_value'),
                'loanType': fields.String(attribute='loan_type'),
                'authors': fields.List(fields.Nested(Author.simple_fields()), attribute='authors'),
                'samples': fields.List(fields.Nested(Sample.simple_fields()), attribute='samples'),
                'popularity': fields.Integer(attribute='popularity'),
                }


    @staticmethod
    def get(id):
        a_book = Book.query.get(id)
        if a_book:
            return a_book.get_without_sample_erased

    @property
    def get_without_sample_erased(self):
        not_erased_samples_list = self.samples
        for a_sample in self.samples:
            if not a_sample.erased:
                not_erased_samples_list.append(a_sample)
        self.samples = not_erased_samples_list
        return self

    @staticmethod
    def get_all():
        return Book.query.filter_by(erased=False).all()

    @staticmethod
    def get_all_order_by_popularity():
        book_list = Book.query.filter_by(erased=False).all()
        if book_list:
            return book_list.sort(key=lambda x: x.popularity, reverse=True)
        else:
            return []
        

    @staticmethod
    def create_author_assoc(book_id, author_id):
        a_book = Book.query.get(book_id)
        if a_book:
            a_author = Author.query.get(author_id)
            if not (a_author in a_book.authors):
                a_book.authors.append(a_author)
                db.session.commit()  
            else:
                return { 'message' : 'Autor no encontrado.' }, 400    
        else:
            return { 'message' : 'Libro no encontrado.' }, 400

        return {'message' : 'Asociacion entre libro y autor generada.' }, 200

    @staticmethod
    def delete_author_assoc(book_id, author_id):
        a_book = Book.query.get(book_id)
        if a_book:
            a_author = Author.query.get(author_id)
            if (a_author in a_book.authors):
                a_book.authors.remove(a_author)
                db.session.commit()  
            else:
                return { 'message' : 'Autor no encontrado.' }, 400    
        else:
            return { 'message' : 'Libro no encontrado.' }, 400

        return { 'message' : 'Asociacion entre libro y autor eliminada.' }, 200
    
    @staticmethod
    def create(title, 
              publisher, 
              edition_year, 
              edition_country, 
              price, 
              isbn, 
              gender,
              reputation_value, 
              loan_type):
        has_one = Book.query.filter_by(isbn=isbn).first()
        if has_one:
            return has_one    
        new_book = Book(title=title, 
                        publisher=publisher,  
                        edition_year=edition_year, 
                        edition_country=edition_country, 
                        price=price, 
                        isbn=isbn,
                        gender=gender, 
                        reputation_value=reputation_value,
                        loan_type=loan_type)   
        db.session.add(new_book)
        db.session.commit()
        return new_book

    @staticmethod
    def update(id, 
              title, 
              publisher, 
              edition_year, 
              edition_country, 
              price, 
              isbn,
              gender, 
              reputation_value, 
              loan_type):
        book = Book.query.get(id)
        if book:
            book.title = title 
            book.publisher = publisher 
            book.edition_year = edition_year 
            book.edition_country = edition_country
            book.price = price
            book.isbn = isbn
            book.gender = gender
            book.reputation_value = reputation_value
            book.loan_type = loan_type
        db.session.commit()
        return book

    @staticmethod
    def delete(id):
        book = Book.query.get(id)
        if book:
            book.authors = []
            for sample in book.samples:
                if sample.is_loaned:
                    return { 'message' : 'El libro tiene el ejemplar, con el codigo de barra: ' + sample.bar_code + ' ya prestado' }, 400
                Sample.delete(sample.id)
            book.erased = True
            #db.session.delete(book)
            db.session.commit()
        return book

    @property
    def popularity(self):
        book_loans_count = 0
        for sample in self.samples:
            book_loans_count = sample.loans_count + book_loans_count 
        return book_loans_count
