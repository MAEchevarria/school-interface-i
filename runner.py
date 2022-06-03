from classes.school import School 
from classes.student import Student
from classes.staff import Staff

school = School('Ridgemont High') 
print(school.staff)
print(school.students)
# student_info = {'name' : 'mike', 'password' : 'BigMike', 'school_id' : 12345, 'age' : 30, 'role' : 'Student'}
# mike = Student(**student_info)
# mike = Student("Mike", "30", "student", "BigMike", "10101")
# mick = Staff("Mick", "31", "student", "BigMike", "10101")
# print(mike)
# mike.all_students()