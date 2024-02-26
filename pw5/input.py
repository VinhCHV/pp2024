from domains import Student, Course
import os
import gzip
def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_mark(course_name, student_name):
    return float(input("Enter mark for {}: ".format(student_name)))

def input_choice():
    return input("Enter your choice (1-8): ")

def input_student_info(student_catalog : list, num_students : int ):
    file = open("Student.txt","a")
    file.write("student_catalog"+ "\n")
    for i in range(num_students):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        dob = input("Enter student DoB: ")
        newStudent = Student(name, id, dob)
        student_catalog.append(newStudent)
        file.write(student_catalog[i].get_name() +" " + student_catalog[i].get_id() + " " + student_catalog[i].get_dob() + "\n")
    file.write("student_catalog_end")
    file.close()


def input_student_info_file(student_catalog,num_students):
    file_path = "Students.gzip"
    with open(file_path,"rb") as file:
        file_content = file.read()
        decompressed_content = gzip.decompress(file_content).decode()
        start_index = decompressed_content.find("student_catalog")
        end_index = decompressed_content.find("student_catalog_end")
        if start_index != -1 and end_index != -1:
            start_index = decompressed_content.find('\n', start_index) + 1
            end_index = decompressed_content.rfind('\n', 0, end_index)

            extracted_content = decompressed_content[start_index:end_index].strip()
            lines = extracted_content.split("\n")
            for line in lines:
                values = line.split(" ")
                name = values[0]
                id   = values[1]
                dob  = values[2]
                newStudent = Student(name,id,dob)
                student_catalog.append(newStudent)

def input_mark_file(course_catalog, student_catalog):
    file_path = "Students.gzip"
    with open(file_path,"rb") as file:
        file_content = file.read()
        decompressed_content = gzip.decompress(file_content).decode()
        start_index = decompressed_content.find("mark_start")
        end_index = decompressed_content.find("mark_end")
        if start_index != -1 and end_index != -1:
            start_index = decompressed_content.find('\n', start_index) + 1
            end_index = decompressed_content.rfind('\n', 0, end_index)

            extracted_content = decompressed_content[start_index:end_index].strip()
            lines = extracted_content.split("\n")
            for line in lines:
                values = line.split(" ")
                student = values[0]
                course = values[1]
                mark = values[2]
                for cr in course_catalog:
                    if course == cr.get_name():
                        for std in student_catalog:
                            if student == std.get_name():
                                cr.input_mark(std , mark)

            
def input_course_info_file(course_catalog,num_courses):
     file_path = "Students.gzip"
     with open(file_path,"rb") as file:
        file_content = file.read()
        decompressed_content = gzip.decompress(file_content).decode()
        start_index = decompressed_content.find("course_catalog")
        end_index = decompressed_content.find("course_catalog_end")
        if start_index != -1 and end_index != -1:
            start_index = decompressed_content.find('\n', start_index) + 1
            end_index = decompressed_content.rfind('\n', 0, end_index)
            extracted_content = decompressed_content[start_index:end_index].strip()
            lines = extracted_content.split("\n")
            for line in lines:
                values = line.split(" ")
                name = values[0]
                id   = values[1]
                newCourse = Course(name,id)
                course_catalog.append(newCourse)


def input_course_info(course_catalog : list, num_courses : int):
    file = open("Course.txt", "a")
    file.write("course_catalog" + "\n")
    for i in range(num_courses):
                coursename = input("Enter course name: ")
                courseid = input("Enter course ID: ")
                newCourse = Course(coursename, courseid)
                course_catalog.append(newCourse)
                file.write(course_catalog[i].get_name() +" " +  course_catalog[i].id + "\n" )
    file.write("course_catalog_end")
    file.close()
    


