import numpy as np
import math

class Student:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

    def getName(self):
        return self.name


class Course:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.mark = {}

    def getName(self):
        return self.name

    def inputmark(self, student, mark):
        self.mark[student.name] = mark

    def givemark(self):
        if len(self.mark) == 0:
            return "no mark input"
        else:
            return self.mark

    def get_new(self, variable_name):
        return getattr(self, variable_name, None)


def input_number_of_students():
    return int(input("Enter the number of students in the class: "))


def input_number_of_courses():
    return int(input("Enter the number of courses: "))


def addCredit(course):
    credit = int(input("Enter Credit: " + course.getName()))
    course.Credit = credit


def calcavg(Course_catalog, student_catalog, option):
    if option:
        student = input("Enter a student to calculate GPA: ")
        credits = np.array([course.get_new("Credit") for course in Course_catalog])
        credits = credits.astype(float)
        markarray = np.array([i.givemark()[student] for i in Course_catalog])
        markarray = markarray.astype(float)
        weighted_sum = np.sum(credits * markarray)
        total_credits = np.sum(credits)
        return str(math.floor(weighted_sum / total_credits))
    else:
        gpalist = []
        credits = np.array([course.get_new("Credit") for course in Course_catalog])
        credits = credits.astype(float)
        for j in student_catalog:
            markarray = np.array([i.givemark()[j.getName()] for i in Course_catalog])
            markarray = markarray.astype(float)
            weighted_sum = np.sum(credits * markarray)
            total_credits = np.sum(credits)
            gpalist.append(int(weighted_sum / total_credits))
        return gpalist


def input_number():
    num_students = input_number_of_students()
    num_courses = input_number_of_courses()
    while num_students < 0 or num_courses < 0:
        print("Invalid input, input again")
        num_students = input_number_of_students()
        num_courses = input_number_of_courses()
    return num_students, num_courses


def sorting(Course_catalog, Student_catalog):
    Gpalist = calcavg(Course_catalog, Student_catalog, option=False)
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

    num_students, num_courses = input_number()

    for i in range(num_students):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        dob = input("Enter student DoB: ")
        newStudent = Student(name, id, dob)
        student_catalog.append(newStudent)

        if i == 0:
            for _ in range(num_courses):
                coursename = input("Enter course name: ")
                courseid = input("Enter course ID: ")
                newCourse = Course(coursename, courseid)
                course_catalog.append(newCourse)

    while True:
        print("\n--- MENU ---")
        print("1. Input student marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Exit")
        print("6. Add credits")
        print("7. GPA")
        print("8. Sort")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            coursechosen = input("Choose course name: ")
            for i in range(num_courses):
                if coursechosen == course_catalog[i].getName():
                    for j in range(num_students):
                        mark = float(input("Enter mark for " + student_catalog[j].getName() + ": "))
                        course_catalog[i].inputmark(student_catalog[j], math.floor(mark))

        if choice == "2":
            for i in range(num_courses):
                name = course_catalog[i].getName()
                print(name)

        if choice == "3":
            for i in range(num_students):
                name = student_catalog[i].getName()
                print(name)

        if choice == "4":
            coursechosen = input("Choose course name: ")
            for i in range(num_courses):
                if coursechosen == course_catalog[i].getName():
                    marks = course_catalog[i].givemark()
                    for student, mark in marks.items():
                        print("Student:", student, "Mark:", mark)

        if choice == "5":
            print("Goodbye!")
            break

        if choice == "6":
            for i in range(num_courses):
                addCredit(course_catalog[i])

        if choice == "7":
            option = True
            print("GPA: ", calcavg(course_catalog, student_catalog, option))

        if choice == "8":
            sorted_GPA = sorting(course_catalog, student_catalog)
            print("Sorted GPA: ", sorted_GPA)


if __name__ == "__main__":
    main()