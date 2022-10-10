
# System Modules
import datetime

# Third Party Modules
import marshmallow as ma
import sqlalchemy as db

def get_timestamp():
    """Returns the current timestamp"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    middle_name = db.Column(db.String(80), nullable=True)
    birth_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PersonSchema(ma.Schema):
    class Meta:
        model = Person
        sqla_session = db.session