import tkinter as tk
from tkinter import messagebox

class Manager ():
    def __init__(self, code=None, name=None, email=None, password=None, gender=None, dob=None, mobNo=None) -> None:
        self._code = code
        self._name = name
        self._email = email
        self._password = password
        self._gender = gender
        self._dob = dob
        self._mobNo = mobNo
        self._role = 'Manager'

    def update_manager_data():
        # Get the updated values from the form
        updated_name = entry_name.get()
        updated_email = entry_email.get()
        updated_password = entry_password.get()
        updated_gender = entry_gender.get()
        updated_dob = entry_dob.get()
        updated_mob_no = entry_mob_no.get()

        # Update the Manager instance with the new values
        manager_instance._name = updated_name
        manager_instance._email = updated_email
        manager_instance._password = updated_password
        manager_instance._gender = updated_gender
        manager_instance._dob = updated_dob
        manager_instance._mobNo = updated_mob_no

        # Show a message box indicating that the update was successful
        messagebox.showinfo("Update Successful", "Manager data updated successfully!")

    # Function to go back to the main menu
    def exit():
        root.destroy()  # Destroy the current window (update form)
        
    def update_profile(ob):
        root = tk.Tk()
        root.title("Update Manager Data")
        
        # Create Manager instance (replace with actual data)
        global manager_instance
        manager_instance = ob
        
        # Create form elements
        label_name = tk.Label(root, text="Name:")
        label_email = tk.Label(root, text="Email:")
        label_password = tk.Label(root, text="Password:")
        label_gender = tk.Label(root, text="Gender:")
        label_dob = tk.Label(root, text="Date of Birth:")
        label_mob_no = tk.Label(root, text="Mobile Number:")

        entry_name = tk.Entry(root)
        entry_name.insert(0, manager_instance._name)

        entry_email = tk.Entry(root)
        entry_email.insert(0, manager_instance._email)

        entry_password = tk.Entry(root)
        entry_password.insert(0, manager_instance._password)

        entry_gender = tk.Entry(root)
        entry_gender.insert(0, manager_instance._gender)

        entry_dob = tk.Entry(root)
        entry_dob.insert(0, manager_instance._dob)

        entry_mob_no = tk.Entry(root)
        entry_mob_no.insert(0, manager_instance._mobNo)

        btn_update = tk.Button(root, text="Update", command=lambda: return_updated_manager(manager_instance))
        btn_exit = tk.Button(root, text="Exit", command=exit)

        # Arrange form elements using grid layout
        label_name.grid(row=0, column=0, sticky=tk.E)
        entry_name.grid(row=0, column=1)

        label_email.grid(row=1, column=0, sticky=tk.E)
        entry_email.grid(row=1, column=1)

        label_password.grid(row=2, column=0, sticky=tk.E)
        entry_password.grid(row=2, column=1)

        label_gender.grid(row=3, column=0, sticky=tk.E)
        entry_gender.grid(row=3, column=1)

        label_dob.grid(row=4, column=0, sticky=tk.E)
        entry_dob.grid(row=4, column=1)

        label_mob_no.grid(row=5, column=0, sticky=tk.E)
        entry_mob_no.grid(row=5, column=1)

        btn_update.grid(row=6, columnspan=2, pady=10)
        btn_exit.grid(row=7, columnspan=2, pady=10)

        # Run the main event loop
        root.mainloop()

    def add_project():
        # Implement logic for adding a project
        pass

    def view_all_projects():
        # Implement logic for viewing all projects
        pass

    def delete_project():
        # Implement logic for deleting a project
        pass

    def update_project():
        # Implement logic for updating a project
        pass

    def add_bug():
        # Implement logic for adding a bug
        pass

    def view_all_bugs():
        # Implement logic for viewing all bugs
        pass

    def update_bug():
        # Implement logic for updating a bug
        pass

    def delete_bug():
        # Implement logic for deleting a bug
        pass

    def exit_program():
        root.destroy()

# Create the main UI window
root = tk.Tk()
root.title("Manager Module")

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# Create menu items
manager_panel_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Manager Panel", menu=manager_panel_menu)
manager_panel_menu.add_command(label="Update Profile", command=update_profile)

manage_project_menu = tk.Menu(manager_panel_menu, tearoff=0)
manager_panel_menu.add_cascade(label="Manage Project", menu=manage_project_menu)
manage_project_menu.add_command(label="Add Project", command=add_project)
manage_project_menu.add_command(label="View All Projects", command=view_all_projects)
manage_project_menu.add_command(label="Delete Project", command=delete_project)
manage_project_menu.add_command(label="Update Project", command=update_project)

bugs_menu = tk.Menu(manager_panel_menu, tearoff=0)
manager_panel_menu.add_cascade(label="Bugs", menu=bugs_menu)
bugs_menu.add_command(label="Add New Bug", command=add_bug)
bugs_menu.add_command(label="View All Bugs", command=view_all_bugs)
bugs_menu.add_command(label="Update Bug", command=update_bug)
bugs_menu.add_command(label="Delete Bug", command=delete_bug)

menu.add_separator()
menu.add_command(label="Exit", command=exit_program)

# Run the main event loop
root.mainloop()
