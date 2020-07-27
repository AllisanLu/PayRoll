from FileHandler import *


class Employee:
    def __init__(self, name="", fname = "", salary=7.25, file="None"):
        self.name = name
        self.filename = fname
        self.salary = salary
        self.attendance = file

    def get_attendence_file(self):
        return self.attendance

    def set_attendence_file(self, attendence):
        self.attendance = attendence

    def manage_employee(self, salary, name):
        self.salary = salary
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_filename(self):
        return self.filename

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

