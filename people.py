# Data to serve with our API

PEOPLE = {
    {
        "id": 1,
        "name": "Adge",
        "first_name": "Adriaan",
        "last_name": "Denkers",
        "middle_name": "Harold",
        "suffix": "",
        "birth_date": "1977-11-22 08:45:22-0500"
    },
    {
        "id": 2,
        "name": "Becky",
        "first_name": "Rebecca",
        "last_name": "Denkers",
        "middle_name": "Lydia",
        "suffix": "",
        "birth_date": "1978-08-19 14:02:22-0400"
    },
    {
        "id": 3,
        "name": "Fitz",
        "first_name": "Fitzgerald",
        "last_name": "Denkers",
        "middle_name": "Adriaan",
        "suffix": "",
        "birth_date": "2010-09-08 14:19:22-0400"
    }
}

import connexion
import sqlalchemy as db
from sqlalchemy import create_engine
import sqlite3

# SQLAlchemy model

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    middle_name = db.Column(db.String(80))
    suffix = db.Column(db.String(80))
    birth_date = db.Column(db.DateTime, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# from models import Person
# people = Person.query.order_by(Person.name).all()
# for person in people:
#     print(f'{person.first_name} {person.last_name}, dob: {person.birth_date}')