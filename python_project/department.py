class Department:
    """
    Represents a specific hospital department.
    Manages assigned staff members and admitted patients.
    """

    def __init__(self, name: str):
        """
        Constructor method to initialize a Department instance.

        Parameters:
            name (str): The name of the department (e.g., 'ICU', 'Cardiology').

        Attributes initialized:
            self.name (str): Stores department name.
            self.patients (list): Stores Patient objects assigned to this department.
            self.staff (list): Stores Staff objects assigned to this department.
        """
        self.name = name
        self.patients = []  # List[Patient]
        self.staff = []     # List[Staff]

    def add_patient(self, patient: object):
        """
        Appends a patient object to the department's patient list.

        Parameters:
            patient (Patient): The patient object to be added.
        """
        self.patients.append(patient)

    def add_staff(self, staff_member: object):
        """
        Appends a staff member object to the department's staff list.

        Parameters:
            staff_member (Staff): The staff object to be added.
        """
        self.staff.append(staff_member)

    def display_patients(self):
        """
        Iterates through and displays information for all patients in this department.
        Uses duck typing to call view_record() if defined, falling back to basic printing.
        """
        print(f"patients in {self.name} Department:")
        for patients in self.patients:
            if hasattr(patients, 'view_record'):
                patients.view_record()
            else:
                print(patients.view_record())

    def display_staff(self):
        """
        Iterates through and displays information for all staff members in this department.
        Uses duck typing to call view_info() if available, falling back to basic printing.
        """
        print(f"Staff in {self.name} Department:")
        for staff_member in self.staff:
            if hasattr(staff_member, 'view_info'):
                staff_member.view_info()
            else:
                print(staff_member)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the Department object.

        Returns:
            str: Formatted string containing the department name.
        """
        return f"Department: {self.name}"
