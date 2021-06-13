from psycopg2 import extras
from flask import Response, request, abort
from db import get_connection
from json import dumps, loads


def index():
    connection = get_connection()
    cursor = connection.cursor(cursor_factory= extras.RealDictCursor )
    cursor.execute(
        'SELECT books.id, books.title,'
        ' authors.author_name from authors'
        ' right join books on authors.id >= 1')

    return Response(dumps(cursor.fetchall()), mimetype='application/json')

def add():
    data = loads(request.data.decode('utf-8'))
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books(title, author_id) VALUES(%s, %s) RETURNING id',
                   (data['title'], data['author_id']))
    book_id = cursor.fetchone()[0]
    connection.commit()
    return Response(dumps({
        'id': book_id
    }), mimetype='application/json', status=201)


def delete(book_id):
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute('SELECT id, title, author_id FROM books WHERE id=%s', (book_id))
    author = cursor.fetchone()
    if author is None:
        abort(404)
    cursor.execute('DELETE FROM books WHERE id=%s', (book_id))
    connection.commit()
    return Response(dumps({
        'status': 'ok'
    }), mimetype='aplication/json', status=200)
