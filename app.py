from flask import Flask
from api import authors, books


app = Flask(__name__)

app.add_url_rule('/authors', view_func=authors.index_authors, methods=['GET'])
app.add_url_rule('/books', view_func=books.index_books, methods=['GET'])

app.add_url_rule('/authors', view_func=authors.add_author, methods=['POST'])
app.add_url_rule('/books', view_func=books.add_book, methods=['POST'])

app.add_url_rule('/authors/<author_id>', view_func=authors.delete_author, methods=['DELETE'])
app.add_url_rule('/books/<book_id>', view_func=books.delete_book, methods=['DELETE'])
