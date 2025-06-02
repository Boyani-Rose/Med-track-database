# lib/db/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email= Column(String)
    contact= Column(Integer)


    prescriptions = relationship("Prescription", back_populates="user")
    medications = relationship("Medication", back_populates="user")

class Drug(Base):
    __tablename__ = 'drugs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    prescriptions = relationship("Prescription", back_populates="drug")

class Prescription(Base):
    __tablename__ = 'prescriptions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    drug_id = Column(Integer, ForeignKey('drugs.id'))
    frequency = Column(String)
    prescribed_at = Column(DateTime, default=datetime.utcnow)
    duration_in_days = Column(Integer)

    user = relationship("User", back_populates="prescriptions")
    drug = relationship("Drug", back_populates="prescriptions")
    medication = relationship("Medication", back_populates="prescription", uselist=False)

class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    prescription_id = Column(Integer, ForeignKey('prescriptions.id'))
    status = Column(String)
    total_doses = Column(Integer)
    doses_taken = Column(Integer)

    user = relationship("User", back_populates="medications")
    prescription = relationship("Prescription", back_populates="medication")
