import os
from config import db       # imports db instance from config.py
from models import Person   # imports Person class from models.py

# Data to initialize database with
PEOPLE = [
    {
        "id": 1,
        "name": "Adge",
        "first_name": "Adriaan",
        "last_name": "Denkers",
        "middle_name": "Harold",
        "suffix": "",
        "birth_date": "1977-11-22 08:45:22-0500",
        "age": 45
    },
    {
        "id ": 2,
        "name": "Becky",
        "first_name": "Rebecca",
        "last_name": "Denkers",
        "middle_name": "Lydia",
        "suffix": "",
        "birth_date": "1978-08-19 14:02:22-0400",
        "age": 45
    },
    {
        "id": 3,
        "name": "Fitz",
        "first_name": "Fitzgerald",
        "last_name": "Denkers",
        "middle_name": "Adriaan",
        "suffix": "",
        "birth_date": "2010-09-08 14:19:22-0400",
        "age": 12
    }
]

# Delete the database file if it exists currently
if os.path.exists("people.db"):
    os.remove("people.db")

#Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(person_id=person["person_id"], name=person["name"], first_name=person["first_name"], last_name=person["last_name"], middle_name=person["middle_name"], suffix=person["suffix"], birth_date=person["birth_date"], age=person["age"])
    db.session.add(p)   # despite doing db.session.add(p), we've only added p to the database session, not the database itself

# Commit changes to the database
db.session.commit()