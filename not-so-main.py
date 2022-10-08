# author: adge denkers | https://github.com/adgedenkers/
# created: 2021-03-31 15:50:00


# Path: main.py
from importlib import resources
import pandas as pd
from treelib import Tree
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# relationship tables

patient_medication = Table(
    "patient_medication",
    Base.metadata,
    Column("patient_id", Integer, ForeignKey("patient.id")),
    Column("medication_id", Integer, ForeignKey("medication.id"))
)

patient_practicioner = Table(
    "patient_practicioner",
    Base.metadata,
    Column("patient_id", Integer, ForeignKey("patient.id")),
    Column("practicioner_id", Integer, ForeignKey("practicioner.id"))
)

medication_medicationform = Table(
    "medication_medicationform",
    Base.metadata,
    Column("medication_id", Integer, ForeignKey("medication.id")),
    Column("medicationform_id", Integer, ForeignKey("medicationform.id"))
)

# classes

class Practicioner(Base):
    __tablename__ = "practicioner"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    patients = relationship("Patient", backref="practicioner")

class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    birth_date = Column(String)
    age = Column(Integer)
    practicioners = relationship(
        "Practicioner", secondary="patient_practicioner", back_populates="patients"
    )
    medications = relationship(
        "Medication", secondary="patient_medication", back_populates="patients"
    )


class MedicationForm(Base):
    __tablename__ = 'medication_form'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class Medication(Base):
    __tablename__ = 'medication'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("Patient", backref=backref('medication', order_by=id))
    generic_name = Column(String)
    brand_name = Column(String)
    medication_form = relationship(
        "MedicationForm", secondary="medication_medicationform", backref="medications"
    )
    individual_dose = Column(String)
    units = Column(String)
    medication_form_id = Column(Integer, ForeignKey('medication_form.id'))
    route = Column(String)
    drug_class = Column(String)
    description = Column(String)
    url = Column(String)

def get_medications_by_patient(session, ascending=True):
    """Get a list of patients and the number of medications they're taking

    Args:
        session: database session to use

    Returns:
        List: list of patients sorted by number of medications
    """
    return (
        session.query(
            Patient.name,
            func.count(Medication.name).label("total_medications"),
        )
        .join(Patient.medications)
        .group_by(Patient.name)
        .order_by(asc("total_medications"))
    )

def main():
    with resources.path(
        "project.data", "infinitum.db"
    ) as sqlite_filepath:
        engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # get the number of medications for each patient
    medications_by_patient = get_medications_by_patient(session)
    for row in medications_by_patient:
        print(row)
    print()

    # get the number of practicioners for each patient
    practicioners_by_patient = get_practicioners_by_patient(session)
    for row in practicioners_by_patient:
        print(f'Practicioner: {row.name}')
    print()
