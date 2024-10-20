from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Author, Book
from datetime import datetime
import secrets
import os

app = Flask(__name__)

# Set the secret key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(16))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digital_library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the app
db.init_app(app)

@app.route('/')
def home():
    search_term = request.args.get('search', '')
    if search_term:
        search = f"%{search_term}%"
        books = Book.query.join(Author).filter(
            (Book.title.ilike(search)) | (Author.name.ilike(search))
        ).all()
    else:
        books = Book.query.all()

    return render_template('home.html', books=books)

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_detail.html', book=book)

@app.route('/author/<int:author_id>')
def author_detail(author_id):
    author = Author.query.get_or_404(author_id)
    return render_template('author_detail.html', author=author)

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form.get('birth_date')  # Use .get() to avoid KeyError

        # Convert birth date to date object
        if birth_date:
            try:
                birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid date format for birth date. Please use YYYY-MM-DD.')
                return redirect(url_for('add_author'))
        else:
            birth_date = None

        new_author = Author(name=name, birth_date=birth_date)
        db.session.add(new_author)
        db.session.commit()
        flash('Author added successfully!')
        return redirect(url_for('home'))

    return render_template('add_author.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author_id = request.form['author_id']
        published_date = request.form['published_date']

        # Convert published date to date object
        if published_date:
            try:
                published_date = datetime.strptime(published_date, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid date format. Please use YYYY-MM-DD.')
                return redirect(url_for('add_book'))
        else:
            published_date = None

        author = Author.query.get(author_id)
        if not author:
            flash('Invalid author selected.')
            return redirect(url_for('add_book'))

        new_book = Book(title=title, author_id=author_id, published_date=published_date)
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully!')
        return redirect(url_for('home'))

    authors = Author.query.all()
    return render_template('add_book.html', authors=authors)

@app.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    author_id = book.author_id
    db.session.delete(book)
    db.session.commit()

    # Check if the author has any other books
    if not Book.query.filter_by(author_id=author_id).count():
        author = Author.query.get(author_id)
        db.session.delete(author)
        db.session.commit()
        flash('Book and author deleted successfully!')
    else:
        flash('Book deleted successfully!')

    return redirect(url_for('home'))

with app.app_context():
    db.create_all()  # Create database tables if they don't exist

if __name__ == '__main__':
    app.run(debug=True)
