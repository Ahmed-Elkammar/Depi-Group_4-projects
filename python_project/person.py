class Person:
    """
    Base class representing a person in the hospital system.

    Attributes:
        name (str): The full name of the person (alphabetic characters only).
        age (int): The age of the person (must be a positive integer).
    """
    def __init__(self, name : str , age : int ):
        """
        Initialize a new Person instance with validation.

        Args:
            name (str): The name of the person. Must not be empty and contain only letters and spaces.
            age (int or str): The age of the person. Must be a positive integer greater than zero.

        Raises:
            ValueError: If `name` is empty or contains non-alphabetic characters.
            ValueError: If `age` is empty, not a valid integer, or less than or equal to zero.
        """ 
        if not name or not name.replace(" ","").isalpha():
            raise ValueError("name can't be empty and must contain only alphabetic characters.")
        if not str(age).strip().isdigit() or int(str(age).strip()) <= 0:
            raise ValueError("Age must be a positive integer and cannot be empty.")

        self.name = name 
        self.age = age

    def view_info(self):
        """View basic information about the person."""
        return f"Name: {self.name}, Age: {self.age}"

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
