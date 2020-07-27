class HR:

    def __init__(self):
        self.employees = []

    def generate_salary_slips(self):
        for employee in self.employees:
            employee.calculate_salary()
            #email and format them??

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees
