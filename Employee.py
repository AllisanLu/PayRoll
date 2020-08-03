class Employee:
    def __init__(self, name="", fname = "", salary=7.25, file="None", hours=0, bonus=0, deduction=0):
        self.name = name
        self.filename = fname
        self.salary = salary
        self.attendance = file
        self.hours = hours
        self.bonus = bonus
        self.deduction = deduction

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

    def get_hours(self):
        return self.hours

    def set_hours(self, hours):
        self.hours = hours

    def get_bonus(self):
        return self.bonus

    def set_bonus(self, bonus):
        self.bonus = bonus

    def get_deduction(self):
        return self.deduction

    def set_deduction(self, deduction):
        self.deduction = deduction

