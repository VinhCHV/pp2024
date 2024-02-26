from domains import Student
import sys

if 'domains' in sys.modules:
    print("example_module is imported")
else:
    print("example_module is not imported")

name = "Vinh"
id= 15
dob =20
newStudent = Student(name,id,dob)
print(newStudent)

