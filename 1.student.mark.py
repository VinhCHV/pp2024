def input_number_of_students():
    return int(input("Enter the number of students in the class: "))


def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return (student_id, student_name, student_dob)


def input_number_of_courses():
    return int(input("Enter the number of courses: "))


def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return (course_id, course_name)


def input_student_marks(students, courses):
    course_id = input("Enter the course ID: ")
    course_index = get_course_index(course_id, courses)
    if course_index == -1:
        print("Course not found!")
        return

    for student in students:
        mark = int(input(f"Enter the mark for {student[1]}: "))
        student[3][course_index] = mark


def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")


def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")


def show_student_marks(students, courses):
    student_id = input("Enter student ID: ")
    student_index = get_student_index(student_id, students)
    if student_index == -1:
        print("Student not found!")
        return

    print(f"Student: {students[student_index][1]}")
    for i, mark in enumerate(students[student_index][3]):
        course_name = courses[i][1]
        print(f"Course: {course_name}, Mark: {mark}")


def show_course_average_mark(students, courses):
    course_id = input("Enter the course ID: ")
    course_index = get_course_index(course_id, courses)
    if course_index == -1:
        print("Course not found!")
        return

    marks = []
    for student in students:
        mark = student[3][course_index]
        marks.append(mark)

    average_mark = sum(marks) / len(marks)
    course_name = courses[course_index][1]
    print(f"Course: {course_name}, Average Mark: {average_mark}")


def show_all_courses_average_mark(students, courses):
    for i, course in enumerate(courses):
        marks = []
        for student in students:
            mark = student[3][i]
            marks.append(mark)

        average_mark = sum(marks) / len(marks)
        course_name = course[1]
        print(f"Course: {course_name}, Average Mark: {average_mark}")


def get_course_index(course_id, courses):
    for i, course in enumerate(courses):
        if course[0] == course_id:
            return i
    return -1


def get_student_index(student_id, students):
    i = 0
    for i, student in enumerate(students):
        if student[0] == student_id:
            return i
    return -1


if __name__ == "__main__":
    students = []
    courses = []

    num_students = input_number_of_students()
    num_courses = input_number_of_courses()

    for _ in range(num_students):
        student_info = input_student_info()
        students.append(list(student_info))
        students[-1].append([0] * num_courses)

    for _ in range(num_courses):
        course_info = input_course_info()
        courses.append(list(course_info))

    while True:
        print("\n--- MENU ---")
        print("1. Input student marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Show average marks for a course")
        print("6. Show average marks for all courses")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            input_student_marks(students, courses)
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            list_students(students)
        elif choice == "4":
            show_student_marks(students, courses)
        elif choice == "5":
            show_course_average_mark(students, courses)
        elif choice == "6":
            show_all_courses_average_mark(students, courses)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")



