from department import Department

class Hospital:
    """Class for managing hospital operations.

        Attributes:
        name (str): The name of the hospital.
        location (str): The location/address of the hospital.
        departments (list): List of registered Department instances.
    """
    def __init__(self, name, location):
        """
        Initialize a new Hospital instance.

        Args:
            name (str): The name of the hospital .
            location (str): The location of the hospital.

        Raises:
            ValueError: If `name` is empty or contains non-alphabetic characters.
            ValueError: If `location` is empty or consists solely of whitespace.
        """

        if not name or not name.replace(" ","").isalpha():
            raise ValueError("name can't be empty and must contain only alphabetic characters.")
        if not location or not str(location).strip():
            raise ValueError("Location cannot be empty.")

        self.name = name
        self.location = location
        self.departments = []  # List to hold departments

    def add_department(self, department):
        """Add a department to the hospital.

            Args:
            department (Department): The department instance to be added.

            Raises:
            TypeError: If `department` is not an instance of the `Department` class.
            ValueError: If a department with the same name already exists in the hospital (case-insensitive).
        """
        if not isinstance(department, Department):
            raise TypeError("Expected an instance of Department.")
        for dept in self.departments:
            if dept.name.lower() == department.name.lower():
                raise ValueError(f"Department '{department.name}' already exists.")
            
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")