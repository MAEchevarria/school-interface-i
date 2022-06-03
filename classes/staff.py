from classes.person import Person
import csv
STAFF_FILE = "data/staff.csv"
class Staff(Person):
    def __init__(self, name, age, role, password, employee_id):
        Person.__init__(self, name, age, role, password)
        self.employee_id = employee_id

    def __str__(self):
        return f"{self.name}"

    def all_staff(self):
        with open(STAFF_FILE, newline = '') as file:
            rows_in_file = csv.DictReader(file)
            staff_list = []
            for row in rows_in_file:
                staff_list.append(Staff(**row))     
            return staff_list