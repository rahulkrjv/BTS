import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
import manager

class Admin ():
    def __init__(self, code=None, name=None, email=None, password=None, gender=None, dob=None, mobNo=None) -> None:
        self._code = code
        self._name = name
        self._email = email
        self._password = password
        self._gender = gender
        self._dob = dob
        self._mobNo = mobNo
        self._role = 'Admin'

    def add_manager(self, cursor):
        if self._role == 'Admin':
            try:
                ob = manager.Manager()
                ob.update_profile()

                qry = f"INSERT INTO Employee Values({ob._code}, '{ob._name}', '{ob._email}', '{ob._password}', '{ob._gender}', '{ob._dob}', {ob._mobNo}, '{ob._role}')"
                cursor.execute(qry)
                con.commit()

            except sql.Error as error:
                print()
                print('Error occurred - ', error)
                print()
                input("Enter any key to Continue.")
            else:
                print()
                print("Successfully Added.")
                print()
                input("Enter any key to Continue.")

    def view_manager(self, cursor):
        # Implement logic for viewing manager accounts
        pass

    def delete_manager(self, cursor):
        # Implement logic for deleting manager account
        pass

    def update_manager(self, cursor):
        # Implement logic for updating manager details
        pass

    def add_employee(self, cursor):
        # Implement logic for adding employee account
        pass

    def view_employee(self, cursor):
        # Implement logic for viewing employee accounts
        pass

    def delete_employee(self, cursor):
        # Implement logic for deleting employee account
        pass

    def update_employee(self, cursor):
        # Implement logic for updating employee details
        pass

    def view_all_projects(self, cursor):
        # Implement logic for viewing all projects
        pass

    def view_bug_reports(self, cursor):
        # Implement logic for viewing bug reports
        pass

    def exit_program():
        root.destroy()

# Create the main UI window
root = tk.Tk()
root.title("Admin Module")

# Connect to DataBase
con = sql.connect("BTS")
cursor = con.cursor()


# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# Create menu items
manager_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Manager", menu=manager_menu)
manager_menu.add_command(label="Add Manager Account", command=add_manager)
manager_menu.add_command(label="View Manager Account", command=view_manager)
manager_menu.add_command(label="Delete Manager", command=delete_manager)
manager_menu.add_command(label="Update Manager Details", command=update_manager)

employee_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Employee", menu=employee_menu)
employee_menu.add_command(label="Add Employee Account", command=add_employee)
employee_menu.add_command(label="View Employee's Account", command=view_employee)
employee_menu.add_command(label="Delete Employee Account", command=delete_employee)
employee_menu.add_command(label="Update Employee Details", command=update_employee)

menu.add_command(label="View All Project", command=view_all_projects)
menu.add_command(label="View Bug's Reports", command=view_bug_reports)
menu.add_separator()
menu.add_command(label="Exit", command=exit_program)

# Run the main event loop
root.mainloop()
