from psycopg2 import extras
from flask import Response, request, abort
from db import get_connection
from json import dumps, loads


def index_authors():
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute('SELECT id, author_name FROM authors')
    return Response(dumps(cursor.fetchall()), mimetype='application/json')


def add_author():
    data = loads(request.data.decode('utf-8'))
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO authors(author_name) VALUES(%s) RETURNING *',
                  (data['author_name'],))
    author_id, author_name = cursor.fetchone()
    connection.commit()
    return Response(dumps({
        'id': author_id,
        'author': author_name
    }), mimetype='application/json', status=201)


def delete_author(author_id):
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute('SELECT id, author_name FROM authors WHERE id=%s', (author_id))
    author = cursor.fetchone()
    if author is None:
        abort(404)
    cursor.execute('DELETE FROM authors WHERE id=%s', (author_id))
    connection.commit()
    return Response(dumps({
        'status': 'ok'
    }), mimetype='aplication/json', status=200)
