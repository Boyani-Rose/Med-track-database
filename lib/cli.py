# cli.py
from lib.db.models import User, Drug, Prescription, Medication
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///meds.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_user():
    name = input("User name: ")
    session.add(User(name=name))
    session.commit()
    print("User added.")

def list_users():
    users = session.query(User).all()
    if users:
        print("\nUsers:")
        for user in users:
            print(f"ID: {user.id} | Name: {user.name}")
    else:
        print("No users found.")

def update_user():
    user_id = int(input("User ID to update: "))
    user = session.get(User, user_id)
    if user:
        new_name = input(f"New name for {user.name}: ")
        user.name = new_name
        session.commit()
        print("User updated.")
    else:
        print("User not found.")

def delete_user():
    user_id = int(input("User ID to delete: "))
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        print("User deleted.")
    else:
        print("User not found.")

def add_drug():
    name = input("Drug name: ")
    desc = input("Description: ")
    session.add(Drug(name=name, description=desc))
    session.commit()
    print("Drug added.")

def list_drugs():
    drugs = session.query(Drug).all()
    if drugs:
        print("\nDrugs:")
        for drug in drugs:
            print(f"ID: {drug.id} | Name: {drug.name} | Description: {drug.description}")
    else:
        print("No drugs found.")

def update_drug():
    drug_id = int(input("Drug ID to update: "))
    drug = session.get(Drug, drug_id)
    if drug:
        new_name = input(f"New name for {drug.name}: ")
        new_desc = input(f"New description (current: {drug.description}): ")
        drug.name = new_name
        drug.description = new_desc
        session.commit()
        print("Drug updated.")
    else:
        print("Drug not found.")

def delete_drug():
    drug_id = int(input("Drug ID to delete: "))
    drug = session.get(Drug, drug_id)
    if drug:
        session.delete(drug)
        session.commit()
        print("Drug deleted.")
    else:
        print("Drug not found.")

def add_prescription():
    user_id = int(input("User ID: "))
    drug_id = int(input("Drug ID: "))
    freq = input("Frequency (e.g. daily): ")
    dur = int(input("Duration (days): "))

    prescription = Prescription(
        user_id=user_id,
        drug_id=drug_id,
        frequency=freq,
        duration_in_days=dur
    )
    session.add(prescription)
    session.commit()

    medication = Medication(
        user_id=user_id,
        prescription_id=prescription.id,
        status="active",
        total_doses=dur,
        doses_taken=0
    )
    session.add(medication)
    session.commit()

    print("Prescription and Medication record added.")

def list_prescriptions():
    prescriptions = session.query(Prescription).all()
    if prescriptions:
        print("\nPrescriptions:")
        for p in prescriptions:
            user_name = p.user.name if p.user else "Unknown User"
            drug_name = p.drug.name if p.drug else "Unknown Drug"
            print(f"ID: {p.id} | User: {user_name} | Drug: {drug_name} | Frequency: {p.frequency} | Duration: {p.duration_in_days} days")
    else:
        print("No prescriptions found.")

def update_prescription():
    pres_id = int(input("Prescription ID to update: "))
    pres = session.get(Prescription, pres_id)
    if pres:
        freq = input(f"New frequency (current: {pres.frequency}): ")
        dur = int(input(f"New duration in days (current: {pres.duration_in_days}): "))
        pres.frequency = freq
        pres.duration_in_days = dur
        session.commit()
        print("Prescription updated.")
    else:
        print("Prescription not found.")

def delete_prescription():
    pres_id = int(input("Prescription ID to delete: "))
    pres = session.get(Prescription, pres_id)
    if pres:
        session.delete(pres)
        session.commit()
        print("Prescription deleted.")
    else:
        print("Prescription not found.")

def record_dose():
    med_id = int(input("Medication ID: "))
    med = session.get(Medication, med_id)
    if med:
        med.doses_taken += 1
        session.commit()
        print(f"Dose recorded. {med.doses_taken}/{med.total_doses} doses taken.")
    else:
        print("Medication not found.")

def update_medication_status():
    med_id = int(input("Medication ID to update status: "))
    med = session.get(Medication, med_id)
    if med:
        new_status = input(f"New status (current: {med.status}): ")
        med.status = new_status
        session.commit()
        print("Medication status updated.")
    else:
        print("Medication not found.")

def delete_medication():
    med_id = int(input("Medication ID to delete: "))
    med = session.get(Medication, med_id)
    if med:
        session.delete(med)
        session.commit()
        print("Medication deleted.")
    else:
        print("Medication not found.")

def exit_program():
    print("Goodbye!")
    exit()

def main():
    while True:
        print("\n--- Medication Tracker CLI ---")
        print("1. Add User")
        print("2. List Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Add Drug")
        print("6. List Drugs")
        print("7. Update Drug")
        print("8. Delete Drug")
        print("9. Add Prescription")
        print("10. List Prescriptions")
        print("11. Update Prescription")
        print("12. Delete Prescription")
        print("13. Record Dose Taken")
        print("14. Update Medication Status")
        print("15. Delete Medication")
        print("0. Exit")

        choice = input("Enter choice: ")

        options = {
            "1": add_user,
            "2": list_users,
            "3": update_user,
            "4": delete_user,
            "5": add_drug,
            "6": list_drugs,
            "7": update_drug,
            "8": delete_drug,
            "9": add_prescription,
            "10": list_prescriptions,
            "11": update_prescription,
            "12": delete_prescription,
            "13": record_dose,
            "14": update_medication_status,
            "15": delete_medication,
            "0": exit_program
        }

        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Please choose a number from the menu.")

if __name__ == "__main__":
    main()
