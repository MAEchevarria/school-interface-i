from classes.person import Person
import csv
STUDENT_FILE = "data/students.csv"
class Student(Person):
    def __init__(self, name, age, role, password, school_id):
        Person.__init__(self, name, age, role, password)
        self.school_id = school_id

    def __str__(self):
        return f"{self.school_id} {self.age} {self.name} {self.password} {self.role}"
    
    def all_students(self):
        with open(STUDENT_FILE, newline = '') as file:
            rows_in_file = csv.DictReader(file)
            students = []
            for row in rows_in_file:
                students.append(Student(**row))
            return students
        