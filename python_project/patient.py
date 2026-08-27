from person import Person

class Patient(Person):
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        return f"Name: {self.name}, Age: {self.age}, Medical Record: {self.medical_record}"