import os
import random
import sqlite3
from pony import orm
from flask import Flask, render_template
from models import db, Employee

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE='peeps.db',
    SECRET_KEY=os.environ.get('SECRET_KEY', 'sekr1t'),
    DEBUG=os.environ.get('DEBUG', False),
    OAUTH_CLIENT_ID=os.environ.get('OAUTH_CLIENT_ID'),
    OAUTH_CLIENT_SECRET=os.environ.get('OAUTH_CLIENT_SECRET'),
    OAUTH_REDIRECT_URI=os.environ.get('OAUTH_REDIRECT_URI'),
))


db.bind('sqlite', app.config['DATABASE'], create_db=True)
db.generate_mapping(create_tables=True)


@app.route('/login/')
def login():
    return kin.authorize(callback=app.config['OAUTH_REDIRECT_URI'])


@orm.core.db_session
def populate_db():
    randint = random.randint(111,999)
    e1 = Employee(given_name='John', 
                  family_name='Doe',
                  email='john{}@example.com'.format(randint),
                  role='Software Developer')
    orm.core.commit()


@app.route('/')
@orm.core.db_session
def index():
    populate_db()
    employees = orm.core.select(e for e in Employee)
    context = dict(employees=employees)
    return render_template('index.html', context=context)

if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=os.environ.get('HTTP_PORT', 8080))
