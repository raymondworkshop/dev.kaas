import sqlite3

import click # create command line interface
from flask import g # store data during an application context
from flask import current_app  # access the application
from flask.cli import with_appcontext

def connect_db():
    """connect to the database. """
    rv = sqlite3.connect(
        current_app.config['DATABASE'],
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    rv.row_factory = sqlite3.Row
    return rv
    

def get_db():
    if 'db' not in g:
        """ connect to the application's configurated database
         the connection is unique for each request and will be reused if this is called again 
        """
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    """ checking if g.db was set and know if a connection was created
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """ return a database connection
    """
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    #db.commit()

@click.command('initdb')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)