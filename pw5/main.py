import gzip
from domains import Student
from domains import Course
from input import (input_number_of_students,input_number_of_courses,input_mark,input_choice,
                   input_student_info,input_student_info_file,input_course_info_file,input_course_info,input_mark_file)
from output import (
    print_course_names, print_student_names, print_student_marks,
    print_gpa, print_sorted_gpa
)
import numpy as np
import math
import os

def calc_avg(course_catalog, student_catalog, option):
    if option:
        student = input("Enter a student to calculate GPA: ")
        credits = np.array([course.get_new("Credit") for course in course_catalog])
        credits = credits.astype(float)
        markarray = np.array([i.givemark()[student] for i in course_catalog])
        markarray = markarray.astype(float)
        weighted_sum = np.sum(credits * markarray)
        total_credits = np.sum(credits)
        return str(math.floor(weighted_sum / total_credits))
    else:
        gpalist = []
        credits = np.array([course.get_new("Credit") for course in course_catalog])
        credits = credits.astype(float)
        for j in student_catalog:
            markarray = np.array([i.givemark()[j.getName()] for i in course_catalog])
            markarray = markarray.astype(float)
            weighted_sum = np.sum(credits * markarray)
            total_credits = np.sum(credits)
            gpalist.append(int(weighted_sum / total_credits))
        return gpalist

def sorting(course_catalog, student_catalog):
    Gpalist = calc_avg(course_catalog, student_catalog, option=False)
    for i in range(1, len(Gpalist)):
        key = Gpalist[i]
        j = i - 1
        while j >= 0 and key < Gpalist[j]:
            Gpalist[j + 1] = Gpalist[j]
            j -= 1
        Gpalist[j + 1] = key
    return Gpalist

def main():
    course_catalog = []
    student_catalog = []
    num_students = input_number_of_students()
    num_courses = input_number_of_courses()
    file_path = "Students.gzip"
    if not os.path.exists(file_path):
        print("compressed file not exist")
    else:
        input_student_info_file(student_catalog,num_students)
        input_course_info_file(course_catalog,num_courses)
        input_mark_file(course_catalog,student_catalog)

    
    input_student_info(student_catalog , num_students )
    input_course_info(course_catalog , num_courses )


    while True:
        print("\n--- MENU ---")
        print("1. Input student marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Exit and compress file")
        print("6. Add credits")
        print("7. GPA")
        print("8. Sort")

        choice = input_choice()

        if choice == "1":
            course_chosen = input("Choose course name: ")
            file = open("Marks.txt", "a")
            file.write("mark_start" + "\n")
            for course in course_catalog:
                if course_chosen == course.get_name():
                    for student in student_catalog:
                        mark = input_mark(course.get_name(), student.get_name())
                        course.input_mark(student, math.floor(mark))
                        file.write(course.get_name() + " " + student.get_name() + " " +  str(mark) + "\n")
            file.write("mark_end")
            file.close()

        if choice == "2":
            print_course_names(course_catalog)

        if choice == "3":
            print_student_names(student_catalog)

        if choice == "4":
            course_chosen = input("Choose course name: ")
            for course in course_catalog:
                if course_chosen == course.get_name():
                    print_student_marks(course)

        if choice == "5":
            for course in course_catalog:
                if course.give_mark() == "no mark input":
                    print ("not input enough mark")
                else:
                    with open("Student.txt", "rb") as student_f_in, open("Course.txt","rb") as course_f_in, open("Marks.txt","rb") as mark_f_in,gzip.open("Students.gzip","wb") as f_out:
                        f_out.write(student_f_in.read())
                        f_out.write(b'\n')
                        f_out.write(course_f_in.read())
                        f_out.write(b'\n')
                        f_out.write(mark_f_in.read())

            print("Goodbye!")
            break

        if choice == "6":
            for course in course_catalog:
                course.add_credit()

        if choice == "7":
            option = True
            print_gpa(calc_avg(course_catalog, student_catalog, option))

        if choice == "8":
            sorted_GPA = sorting(course_catalog, student_catalog)
            print_sorted_gpa(sorted_GPA)

if __name__ == "__main__":
    main()