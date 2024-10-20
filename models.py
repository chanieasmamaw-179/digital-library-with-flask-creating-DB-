from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    """Model for representing authors in the digital library."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)  # Change to nullable=True if appropriate
    date_of_death = db.Column(db.Date, nullable=True)  # Allow NULL values here

    def __init__(self, name, birth_date, date_of_death=None):
        self.name = name
        self.birth_date = birth_date
        self.date_of_death = date_of_death

    def __repr__(self):
        return f'<Author {self.name}>'


class Book(db.Model):
    """Model for representing books in the digital library."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    published_date = db.Column(db.Date, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    def __init__(self, title, published_date, author_id):
        self.title = title
        self.published_date = published_date
        self.author_id = author_id

    def __repr__(self):
        return f'<Book {self.title}>'
