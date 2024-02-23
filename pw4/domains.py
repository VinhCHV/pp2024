class Student:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

    def get_name(self):
        return self.name


class Course:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.mark = {}

    def get_name(self):
        return self.name

    def input_mark(self, student, mark):
        self.mark[student.get_name()] = mark

    def give_mark(self):
        if len(self.mark) == 0:
            return "no mark input"
        else:
            return self.mark

    def get_new(self, variable_name):
        return getattr(self, variable_name, None)

    def add_credit(self):
        credit = int(input("Enter Credit: " + self.get_name()))
        self.Credit = credit