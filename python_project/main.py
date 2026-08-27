'''
main.py
Integration & CLI UI for the Hospital Management System.

Responsibilities:
    - Import all classes (Person, Patient, Staff, Department, Hospital).
    - Create the Hospital object.
    - Provide an interactive menu with modular display options.
    - Add Department / Patient / Staff.
    - Display hospital data (by department, by category, or full view).
    - Handle input errors gracefully.
'''

from person import Person          # noqa: F401 (kept for completeness)
from patient import Patient
from staff import Staff
from department import Department
from hospital import Hospital


def show_menu():
    print("\n" + "=" * 45)
    print("      HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Department")
    print("2. Add Patient")
    print("3. Add Staff")
    print("4. Display Specific Department Data")
    print("5. Display All Patients")
    print("6. Display All Staff")
    print("7. Display Full Hospital Data")
    print("8. Exit")
    print("=" * 45)


def choose_department(hospital):
    '''Lets the user pick an existing department.

    Returns:
        Department instance, or None if there are no departments
        or the user made an invalid choice.
    '''
    if not hospital.departments:
        print("No departments available yet. Please add a department first.")
        return None

    print("\nAvailable Departments:")
    for i, dept in enumerate(hospital.departments, start=1):
        print(f"{i}. {dept.name}")

    choice = input("Choose a department by number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(hospital.departments)):
        print("Invalid department selection.")
        return None

    return hospital.departments[int(choice) - 1]


def add_department(hospital):
    name = input("Enter department name: ").strip()
    try:
        department = Department(name)
        hospital.add_department(department)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


def add_patient(hospital):
    department = choose_department(hospital)
    if department is None:
        return

    name = input("Enter patient name: ").strip()
    age = input("Enter patient age: ").strip()
    medical_record = input("Enter medical record (or leave empty): ").strip() or "None"

    try:
        patient = Patient(name, age, medical_record)
        department.add_patient(patient)
        print(f"Patient '{patient.name}' added to {department.name} department.")
    except ValueError as e:
        print(f"Error: {e}")


def add_staff(hospital):
    department = choose_department(hospital)
    if department is None:
        return

    name = input("Enter staff name: ").strip()
    age = input("Enter staff age: ").strip()
    position = input("Enter staff position: ").strip()

    try:
        staff_member = Staff(name, age, position)
        department.add_staff(staff_member)
        print(f"Staff '{staff_member.name}' added to {department.name} department.")
    except ValueError as e:
        print(f"Error: {e}")


def display_department_data(hospital):
    """Displays patients and staff for a single chosen department."""
    department = choose_department(hospital)
    if department is None:
        return

    print(f"\n=================== {department.name} DEPARTMENT ===================")
    
    if department.patients:
        print(f"Patients in {department.name} department:")
        for patient in department.patients:
            print(" -", patient.view_record())
    else:
        print(f"No patients in {department.name} department.")

    if department.staff:
        print(f"\nStaff in {department.name} department:")
        for staff_member in department.staff:
            print(" -", staff_member)
    else:
        print(f"No staff in {department.name} department.")


def display_all_patients(hospital):
    """Displays all patients across all departments."""
    if not hospital.departments:
        print("No departments registered yet.")
        return

    print("\n================ ALL PATIENTS IN HOSPITAL ================")
    has_patients = False
    for department in hospital.departments:
        if department.patients:
            has_patients = True
            print(f"\nDepartment: {department.name}")
            for patient in department.patients:
                print(" -", patient.view_record())

    if not has_patients:
        print("No patients found in any department.")


def display_all_staff(hospital):
    """Displays all staff members across all departments."""
    if not hospital.departments:
        print("No departments registered yet.")
        return

    print("\n================ ALL STAFF IN HOSPITAL ================")
    has_staff = False
    for department in hospital.departments:
        if department.staff:
            has_staff = True
            print(f"\nDepartment: {department.name}")
            for staff_member in department.staff:
                print(" -", staff_member)

    if not has_staff:
        print("No staff members found in any department.")


def display_hospital_data(hospital):
    """Displays the entire hospital system data."""
    if not hospital.departments:
        print("No departments registered yet.")
        return

    print(f"\n{hospital.name} ({hospital.location})")
    for department in hospital.departments:
        print(f"\n--- {department} ---")

        if department.patients:
            print(f"Patients in {department.name} department:")
            for patient in department.patients:
                print(" -", patient.view_record())
        else:
            print(f"No patients in {department.name} department.")

        if department.staff:
            print(f"Staff in {department.name} department:")
            for staff_member in department.staff:
                print(" -", staff_member)
        else:
            print(f"No staff in {department.name} department.")


def create_hospital():
    """Keeps asking until a valid Hospital is created."""
    while True:
        name = input("Enter hospital name: ").strip()
        location = input("Enter hospital location: ").strip()
        try:
            return Hospital(name, location)
        except ValueError as e:
            print(f"Error: {e}")


def main():
    print("Welcome to the Hospital Management System!")
    hospital = create_hospital()

    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_department(hospital)
        elif choice == "2":
            add_patient(hospital)
        elif choice == "3":
            add_staff(hospital)
        elif choice == "4":
            display_department_data(hospital)
        elif choice == "5":
            display_all_patients(hospital)
        elif choice == "6":
            display_all_staff(hospital)
        elif choice == "7":
            display_hospital_data(hospital)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select a number between 1 and 8.")


if __name__ == "__main__":
    main()