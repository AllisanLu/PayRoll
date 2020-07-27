from Employee import *
from tkinter import *


class FileHandler:

    @staticmethod
    def load_employees(app, file_loc):
        print("Loading " + file_loc)
        # load the employees on file
        try:
            with open(file_loc, 'r') as previous_file:  # opens and closes file for you
                for line in previous_file:
                    employ_nam = StringVar()
                    #split from spaces
                    info = line.split()

                    employ_nam.set(info[0].strip())
                    newbie = Employee(name=employ_nam.get(),
                                      fname=info[1],
                                      salary=info[2],
                                      file=info[3])
                    app.new_person(employ_nam, newbie)
                    app.employee_counter += 1
        except FileNotFoundError:
            print("file not created yet!")

    @staticmethod # think of a way to do this and like be able to save just at the end
    def save(app):
        print("Saving...")
        with open("./save.txt", 'w') as file:
            for i in range(len(app.displayed_employees) - 1):
                file.write(app.displayed_employees[i].get_name() + " " +
                           app.displayed_employees[i].get_filename() + " " +
                           str(app.displayed_employees[i].get_salary()) + " " +
                           app.displayed_employees[i].get_attendence_file() + "\n")

            file.write(app.displayed_employees[-1].get_name() + " " +
                       app.displayed_employees[-1].get_filename() + " " +
                       str(app.displayed_employees[-1].get_salary()) + " " +
                       app.displayed_employees[-1].get_attendence_file())

    @staticmethod
    def load_attendence(app, loc):
        rtn = ""
        try:
            with open(loc, 'r') as file:
                for line in file:
                    rtn += line.strip() + " "
        except FileNotFoundError:
            print("No file found for: attendance")

        return rtn


