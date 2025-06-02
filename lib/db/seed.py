from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User, Drug, Prescription, Medication

engine = create_engine('sqlite:///meds.db')
Session = sessionmaker(bind=engine)
session = Session()




def seed():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    user = User(name="Alice")
    drug = Drug(name="Aspirin", description="Pain reliever")
    prescription = Prescription(user=user, drug=drug, frequency="daily", duration_in_days=30)
    medication = Medication(user=user, prescription=prescription, status="active", total_doses=30, doses_taken=0)

    session.add_all([user, drug, prescription, medication])
    session.commit()
    print("Database seeded!")


if __name__ == "__main__":
    seed()

