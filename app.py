from flask import Flask
from api import authors, books


app = Flask(__name__)

# app.add_url_rule('/authors', view_func=authors.index, methods=['GET'])
app.add_url_rule('/books', view_func=books.index, methods=['GET'])

app.add_url_rule('/books', view_func=books.add, methods=['POST'])
# app.add_url_rule('/books', view_func=books.add, methods=['POST'])

# app.add_url_rule('/authors/<author_id>', view_func=authors.delete, methods=['DELETE'])
app.add_url_rule('/books/<book_id>', view_func=books.delete, methods=['DELETE'])
