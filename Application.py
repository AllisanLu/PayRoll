from FileHandler import *
from HR import *
from Employee import *

from tkinter import *
from tkinter import filedialog
import os
import shutil


class Application:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title(string="Salary Calculator")
        self.root.geometry("260x250")

        self.hr = HR()
        self.string = StringVar()

        self.displayed_employees = []
        self.displayed_names = []

        self.employee_counter = 0

    def set_up(self):
        text = Text(self.root, height=2, width=27)
        text.insert(INSERT, "System: Hello! And welcome!")
        text.pack()

        display = Label(self.root, text="Current employees: ")
        display.pack()

        self.string.set("")

        space = Label(self.root, height=1)
        space.pack(side=BOTTOM)
        employee_button = Button(self.root, text="add employee", fg="purple",
                                 command=self.add_employee)
        employee_button.pack(side=BOTTOM)

        report_button = Button(self.root, text="calculate salary reports", fg="green",
                               command=self.send_reports).pack(side=BOTTOM)

        FileHandler.load_employees(app, "./save.txt")
        self.root.mainloop()

#literally all button commands
    #TODO: what if 2 ppl r trying to edit O.o
    #maybe check to see if the file is opened else where? --> if it is make a error?

    def add_employee(self):
        #menu shows up
        popup = Toplevel(self.root)
        popup.geometry("120x120")
        prompt = Label(popup, text="Pls enter name: ").pack()
        response = Text(popup, height=2, width=10)
        response.pack()

        new_employee = Employee(fname="Employee" + str(self.employee_counter))
        self.employee_counter += 1

        okay = Button(popup, text="OK", command=lambda: self.get_name(response, popup, new_employee))
        okay.pack(side=BOTTOM)

    def get_name(self, response, popup, new_employee):
        new_employee.set_name(response.get("1.0", "end").strip())
        self.hr.add_employee(new_employee)
        name = StringVar()
        name.set(new_employee.get_name())

        self.new_person(name, new_employee)
        FileHandler.save(self)
        popup.destroy()

        #makes a file for the employee
        path = "./" + new_employee.get_filename() + "/"

        try:
            os.makedirs(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

    def delete_employee(self):
        print("delete employees is not ready for use yet")

    def edit_employee(self, employee):
        edit_employee_popup = Toplevel(self.root)
        edit_employee_popup.wm_title("Edit Employee")
        edit_employee_popup.geometry("250x310")
        edit_employee_popup.grab_set()

        name_prompt = Label(edit_employee_popup, text="Name: ").pack()
        name_entry = Text(edit_employee_popup, height=1, width=20)
        name_entry.insert(INSERT, employee.get_name())
        name_entry.pack()

        salary_prompt = Label(edit_employee_popup, text="Salary: ").pack()
        salary_entry = Text(edit_employee_popup, height=1, width=20)
        salary_entry.insert(INSERT, employee.get_salary())
        salary_entry.pack()

        hours_prompt = Label(edit_employee_popup, text="Hours worked: ").pack()
        hours_entry = Text(edit_employee_popup, height=1, width=20)
        hours_entry.insert(INSERT, employee.get_hours())
        hours_entry.pack()

        bonus_prompt = Label(edit_employee_popup, text="Bonus: ").pack()
        bonus_entry = Text(edit_employee_popup, height=1, width=20)
        bonus_entry.insert(INSERT, employee.get_bonus())
        bonus_entry.pack()

        deduction_prompt = Label(edit_employee_popup, text="Deduction: ").pack()
        deduction_entry = Text(edit_employee_popup, height=1, width=20)
        deduction_entry.insert(INSERT, employee.get_deduction())
        deduction_entry.pack()

        filename = StringVar()
        filename.set("File Opened: " + employee.get_attendence_file())
        label_file_explorer = Label(edit_employee_popup, textvariable=filename, wraplength=150)
        label_file_explorer.pack()

        okay = Button(edit_employee_popup, text="OK",
                      command=lambda: self.get_info(name_entry, salary_entry, hours_entry, bonus_entry,
                                                    deduction_entry, edit_employee_popup, employee))
        okay.pack(side=BOTTOM)

        upload = Button(edit_employee_popup, text="upload attendance sheet",
                        command=lambda: self.upload(employee, filename, hours_entry,
                                                    bonus_entry, deduction_entry))
        upload.pack(side=BOTTOM)

    def get_info(self, name_entry, salary_entry, hour_entry, bonus_entry, deduction_entry, popup, employee):
        employee.set_name(name_entry.get("1.0", "end").strip())
        employee.set_salary(salary_entry.get("1.0", "end").strip())
        loc = FileHandler.edit_attendence(employee, hour_entry, bonus_entry, deduction_entry)
        employee.set_attendence_file(loc)
        print("File saved at: " + loc)
        self.update()
        popup.grab_release()
        popup.destroy()

    def upload(self, employee, filename, hour_entry, bonus_entry, deduction_entry):
        #print(os.getcwd())
        file = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                  filetypes=(("Excel File", "*.xlsx*"), ("all files", "*.*")))
        filename.set("File Uploaded: " + file)
        employee.set_attendence_file(file)

        #copy the file
        location = "./" + employee.get_filename() + "/attendance.xlsx"
        shutil.copy2(file, location)
        print("File saved at: " + location)

        FileHandler.save(self)
        FileHandler.load_attendence(self, employee)

        hour_entry.delete('1.0', END)
        bonus_entry.delete('1.0', END)
        deduction_entry.delete('1.0', END)

        hour_entry.insert(INSERT, employee.get_hours())
        bonus_entry.insert(INSERT, employee.get_bonus())
        deduction_entry.insert(INSERT, employee.get_deduction())

    def send_reports(self):
        display = StringVar()
        for employee in self.displayed_employees:
            try:
                FileHandler.load_attendence(app=self, employee=employee)
                amount_paid = (float(employee.get_salary()) * float(employee.get_hours())) + \
                              float(employee.get_bonus()) - float(employee.get_deduction())
                display.set(display.get() + "\n" + employee.get_name() + " is paid: " + str(amount_paid))
            except IndexError:
                print(employee.get_name() + " does not have an attendance file")

        salary_popup = Toplevel(self.root)
        salary_popup.geometry("200x200")
        amounts = Label(salary_popup, textvariable=display).pack()

#smoller functions to be used by others
    def update(self):
        index = 0
        for name in self.displayed_names:
            name.set(self.displayed_employees[index].get_name())
            index += 1
        FileHandler.save(self)

    def new_person(self, name, employee):
        self.displayed_employees.append(employee)
        self.displayed_names.append(name)
        person = Button(self.root, textvariable=name, justify=CENTER,
                        command=lambda: self.edit_employee(employee))
        person.pack(side=LEFT)


if __name__ == '__main__':
    app = Application()
    app.set_up()
