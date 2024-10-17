# Digital Library Application

A simple web application for managing a digital library, built with Flask and SQLAlchemy. This application allows users to add authors and books, search for books or authors, and view detailed information about them.

## Features

- Search for books by title or author.
- View detailed information about each book and author.
- Add new authors and books to the library.
- Delete books (and their authors if no other books exist for that author).

## Requirements

- Python 3.6 or higher
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/digital-library.git
   cd digital-library

    Create a virtual environment and activate it:

    bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:

bash

pip install Flask Flask-SQLAlchemy

Set the SECRET_KEY environment variable for security (optional but recommended):

bash

export SECRET_KEY='your_secret_key'  # On Windows use `set SECRET_KEY='your_secret_key'`

Initialize the database (if not already created). This is handled in the code, but you can manually create the database if necessary:

bash

    flask shell
    from models import db
    db.create_all()
    exit()

Running the Application

To run the application, use the following command:

bash

python app.py

You can then access the application at http://127.0.0.1:5000/ in your web browser.
Usage

    Home Page: Displays a list of all books. You can search for books by entering a title or author in the search bar.
    Add Author: Navigate to the add author page to add a new author to the library.
    Add Book: Navigate to the add book page to add a new book to the library. You need to select an author from the dropdown.
    Book Detail: Click on a book title to view its details, including the author and published date.
    Author Detail: Click on an author's name to view their details and the books they have written.
    Delete Book: You can delete a book, and if the author has no other books, the author will also be deleted.

License

This project is licensed under the Masterschool, Berlin and Asmamaw Yehun License - see the LICENSE file for details.
Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions or bugs.

css


### Notes
- Make sure to update the GitHub URL to point to your repository.
- You can also add a `LICENSE` section if you have a specific license for your project.
- If you have additional features or dependencies, you might want to include those in the README as well.
- contact me chanieasmamaw@yahoo.com or +4917625315666 for any collaborations
