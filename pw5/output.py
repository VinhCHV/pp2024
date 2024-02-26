def print_course_names(course_catalog):
    for course in course_catalog:
        print(course.get_name())

def print_student_names(student_catalog):
    for student in student_catalog:
        print(student.get_name())

def print_student_marks(course):
    marks = course.give_mark()
    for student, mark in marks.items():
        print("Student:", student, "Mark:", mark)

def print_gpa(gpa):
    print("GPA:", gpa)

def print_sorted_gpa(sorted_gpa):
    print("Sorted GPA:", sorted_gpa)