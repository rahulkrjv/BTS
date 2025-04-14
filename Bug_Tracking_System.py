import sqlite3 as sql
import pandas as pd
from prettytable import PrettyTable

try:
    con = sql.connect("BTS")
    cursor = con.cursor()

    qry = '''CREATE TABLE IF NOT EXISTS Employee (
    empCode INT PRIMARY KEY,
    empName VARCHAR(200),
    empEmail VARCHAR(200),
    empPassword VARCHAR(30),
    gender VARCHAR(10),
    DOB DATE,
    mobileNo BIGINT,
    role VARCHAR(20)
);'''

    cursor.execute(qry)
    con.commit()

    qry = '''CREATE TABLE IF NOT EXISTS Project (
    projectID INT PRIMARY KEY,
    projectName VARCHAR(200) NOT NULL,
    SDate DATE NOT NULL,
    EDate DATE NOT NULL,
    projectDec VARCHAR(1000) NULL
);'''

    cursor.execute(qry)
    con.commit()

    qry = '''CREATE TABLE IF NOT EXISTS AssignProject (
    projectID INT NOT NULL,
    empCode INT NOT NULL,
    FOREIGN KEY (projectID)
        REFERENCES Project (projectID),
    FOREIGN KEY (empCode)
        REFERENCES Employee (empCode)
);'''

    cursor.execute(qry)
    con.commit()

    qry = '''CREATE TABLE IF NOT EXISTS BugType (
    bugCode INT PRIMARY KEY,
    bugCatgory VARCHAR(50) NOT NULL,
    bugSeverty VARCHAR(30) NOT NULL
);'''

    cursor.execute(qry)
    con.commit()

    qry = '''CREATE TABLE IF NOT EXISTS BugReport (
    bugNo INT NOT NULL PRIMARY KEY,
    bugCode INT NOT NULL,
    projectID INT NOT NULL,
    TCode INT NULL,
    ECode INT NULL,
    status VARCHAR(20) NOT NULL,
    bugDes VARCHAR(500) NULL,
    FOREIGN KEY (bugCode)
        REFERENCES BugType (bugCode),
    FOREIGN KEY (projectID)
        REFERENCES Project (projectID),
    FOREIGN KEY (TCode)
        REFERENCES Employee (empCode),
    FOREIGN KEY (ECode)
        REFERENCES Employee (empCode)
);'''

    cursor.execute(qry)
    con.commit()

    '''
    qry = f"INSERT INTO Employee(empCode, empName, empEmail, empPassword, gender, DOB, mobileNo , Role) values({12345}, 'Rahul Kumar', 'rahul@outlook.com', 'rahul123', 'Male', '2003-08-29', {9876543201}, 'Admin')"
    cursor.execute(qry)
    con.commit()
    '''

except sql.Error as error:
    print()
    print('Error occurred - ', error)
    print()
    input("Enter any key to Continue.")
    
def display_table(result):
    try:
        if result:
            columns = [desc[0] for desc in cursor.description]
            table = PrettyTable(columns)
            for row in result:
                table.add_row(row)
            print(table)
        else:
            print("No records found.")

    except sql.Error as error:
        print(f"Error occurred - {error}")

# ------------- ADMIN CLASS ---------------


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

    def _display(self):
        print('-' * 12, 'MENU', '-' * 12)
        print('''1. Manager
2. Employee
3. View All Project
4. View Bug's Reports
5. Exit ''')
        print('-' * 30)

    def _Manager(self):
        print('-' * 12, 'MENU', '-' * 12)
        print('''1. Add Manager Account
2. View Manger Account
3. Delete Manager
4. Update Manager Detail's
5. Back ''')
        print('-' * 30)

    def _Employee(self):
        print('-' * 12, 'MENU', '-' * 12)
        print('''1. Add Employee Account
2. View Employee's Account
3. Delete Employee Account
4. Update Employee Detail's
5. Back ''')
        print('-' * 30)

    def _View_All_Project():
        try:
            qry = "Select* from Project"
            cursor.execute(qry)
            result = cursor.fetchall()

        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            display_table(result)
            print()
            input("Enter any key to Continue.")

    def _View_Bugs_Reports():
        try:
            qry = "Select* from BugReport"
            cursor.execute(qry)
            result = cursor.fetchall()

        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            display_table(result, 'BugReport')
            print()
            input("Enter any key to Continue.")

    def _Add_Manager_Account(self):
        if self._role == 'Admin':
            try:
                ob = Manager()
                ob.detailInput()

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

    def _View_Manager_Account(ob):
        try:
            print('-' * 30)
            key = int(input('''1. View All \n 2. View by empCode'''))
            print('-' * 30)
            qry = ''
            if key == 1:
                qry += f"select* from Employee where role = '{'Manager'}' ORDER BY empCode ASC"
            elif key == 2:
                id = int(input('Enter empCode: '))
                qry += f"select* from Employee where empCode = {id}"
            else:
                raise ValueError

            cursor.execute(qry)
            result = cursor.fetchall()

        except ValueError:
            print()
            print("Error! Wrong input.")
            print()
            input("Enter any key to Continue.")
        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            display_table(result, 'Employee')
            print()
            input("Enter any key to Continue.")

    def _Delete_Manager(self):
        try:
            id = int(input("Enter empCode: "))
            if con:
                qry = f"Delete from Employee where empCode = {id}"
                cursor.execute(qry)
                con.commit()

        except ValueError:
            print()
            print("Error! Wrong input type.")
            print()
            input("Enter any key to Continue.")
        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully deleted.")
            print()
            input("Enter any key to Continue.")

    def _Update_Manager_Details(self):
        try:
            ob = Manager()
            ob.detailInput()

            qry = f"UPDATE Employee SET empName = '{ob._name}', empEmail = '{ob._email}', empPassword = '{ob._password}', gender = '{ob._gender}', DOB = '{ob._dob}', mobileNo = {ob._mobNo}, Role = '{ob._role}' WHERE empCode = '{ob._code}'"
            cursor.execute(qry)
            con.commit()

        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully updated.")
            print()
            input("Enter any key to Continue.")

    def _Add_Employee_Account(self):
        try:
            ob = Employee()
            ob.detailInput()
            print('Running')
            print(ob._code)

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

    def _View_Employees_Account(self):
        try:
            print('-' * 30)
            key = int(input('''1. View All \n 2. View by empCode'''))
            print('-' * 30)
            qry = ''
            if key == 1:
                qry += f"select* from Employee where role = 'Developer' or role = 'Tester' ORDER BY empCode ASC"
            elif key == 2:
                id = int(input('Enter empCode: '))
                qry += f"select* from Employee where empCode = {id}"
            else:
                raise ValueError

            cursor.execute(qry)
            result = cursor.fetchall()

        except ValueError:
            print()
            print("Error! Wrong input.")
            print()
            input("Enter any key to Continue.")
        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            display_table(result, 'Employee')
            print()
            input("Enter any key to Continue.")

    def _Delete_Employee_Account(self):
        try:
            id = int(input("Enter empCode: "))
            if con:
                qry = f"Delete from Employee where empCode = {id}"
                cursor.execute(qry)
                con.commit()

        except ValueError:
            print()
            print("Error! Wrong input type.")
            print()
            input("Enter any key to Continue.")
        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully deleted.")
            print()
            input("Enter any key to Continue.")

    def _Update_Employee_Details(self):
        try:
            ob = Employee()
            ob.detailInput()

            qry = f"UPDATE Employee SET empName = '{ob._name}', empEmail = '{ob._email}', empPassword = '{ob._password}', gender = '{ob._gender}', DOB = '{ob._dob}', mobileNo = {ob._mobNo}, Role = '{ob._role}' WHERE empCode = {ob._code}"
            cursor.execute(qry)
            con.commit()

        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully updated.")
            print()
            input("Enter any key to Continue.")

# ------------- MANAGER CLASS ---------------


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

    def detailInput(self):
        try:
            self._code = int(input("Enter empCode: "))
            self._name = input('Enter your Name: ')
            self._email = input('Enter your E-mail: ')
            self._password = input('Enter your Password: ')
            self._gender = input('Enter your Gender: ')
            self._dob = input('Enter your DOB: ')
            self._mobNo = int(input('Enter your mobNo: '))

            if self._code == None or self._name == '' or self._email == '' or self._password == '' or self._gender == '' or self._dob == '' or self._mobNo == None:
                raise ValueError

        except ValueError:
            print("Error! Wrong input.")

    def _display(self):
        print('-' * 12, 'MENU', '-' * 12)
        print('''1. Update Profile
2. Manage Project
3. Bug's
4. Exit
 ''')
        print('-' * 30)

    def _Update_Profile(self):
        try:
            ob = Manager()
            ob.detailInput()

            if self._code == ob._code:
                qry = f"UPDATE Employee SET empName = '{ob._name}', empEmail = '{ob._email}', empPassword = '{ob._password}', gender = '{ob._gender}', DOB = '{ob._dob}', mobileNo = {ob._mobNo}, Role = '{ob._role}' WHERE empCode = {ob._code}"
                cursor.execute(qry)
                con.commit()
            else:
                print("You entered the wrong empCode...")
                return

        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully updated.")
            print()
            input("Enter any key to Continue.")

    def _Manage_Project(self):
        print('-' * 12, 'MENU', '-' * 12)
        print('''1. Add Project
2. View All Projects
3. Delete Project
4. Update Project
5. Back ''')
        print('-' * 30)

    def _bug_Display(self):
        print('-' * 12, 'MENU', '-' * 12)
        print('''1. Add New Bug
2. View All Bug\’s
3. Update Bug
4. Delete Bugs
5. Back ''')
        print('-' * 30)

    def _Add_Project():
        '''
        (projectID int primary key, projectName varchar(30) not null, SDate varchar(30) not null, EDate varchar(30) not null, projectDec varchar(200) not null)
        '''
        try:
            ob = Project()
            ob.detailInput()

            qry = f"INSERT INTO Project Values({ob._projectID}, '{ob._projectName}', '{ob._SDate}', '{ob._EDate}', '{ob._projectDec}')"
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

    def _View_All_Projects():
        ob = Admin()
        ob._View_All_Project()

    def _Delete_Project():
        try:
            id = int(input("Enter projectID: "))
            if con:
                qry = f"Delete from Project where projectID = {id}"
                cursor.execute(qry)
                con.commit()

        except ValueError:
            print()
            print("Error! Wrong input type.")
            print()
            input("Enter any key to Continue.")
        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully deleted.")
            print()
            input("Enter any key to Continue.")

    def _Update_Project():
        try:
            ob = Project()
            ob.detailInput()

            qry = f"UPDATE Project SET projectName = '{ob._projectName}', SDate = '{ob._SDate}', EDate	 = '{ob._EDate}', projectDec = '{ob._projectDec}' WHERE projectID = {ob._projectID}"
            cursor.execute(qry)
            con.commit()

        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully updated.")
            print()
            input("Enter any key to Continue.")

    def _Add_New_Bug():
        try:
            ob = BugType()
            ob.detailInput()

            qry = f"INSERT INTO BugType Values({ob._bugCode}, '{ob._bugCatgory}', '{ob._bugSeverty}')"
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

    def _View_All_Bugs():
        try:
            print('-' * 30)
            key = int(input("Select one: \n1.Bug's Report \n2. Bug type"))
            print('-' * 30)

            qry = ''
            name = ''

            if key == 1:
                qry = "Select* from BugReport"
                name += 'BugReport'
            elif key == 2:
                qry = "Select* from BugType"
                name += 'BugType'
            else:
                raise ValueError

            cursor.execute(qry)
            result = cursor.fetchall()

        except ValueError:
            print()
            print("Error! Wrong input type.")
            print()
            input("Enter any key to Continue.")
        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            display_table(result, name)
            print()
            input("Enter any key to Continue.")

    def _Update_Bug():
        try:
            print('-' * 30)
            key = int(
                input("Select one: \n1.Update Bug's Report \n2.Update Bug type"))
            print('-' * 30)

            if key == 1:
                ob = BugReport()
                ob.detailInput()
                qry = f"UPDATE BugReport SET bugNo = {ob._bugNo}, bugCode = {ob._bugCode}, projectID = {ob._projectID}, TCode = {ob._TCode}, ECode = {ob._ECode}, status = '{ob._status}', bugDes = '{ob._bugDes}'"
            elif key == 2:
                ob = BugType()
                ob.detailInput()
                qry = f"UPDATE BugType SET bugCode = {ob._bugCode}, bugCatgory = '{ob._bugCatgory}', bugSeverty = '{ob._bugSeverty}')"
                cursor.execute(qry)
                con.commit()
            else:
                raise ValueError

        except ValueError:
            print()
            print("Error! Wrong input type.")
            print()
            input("Enter any key to Continue.")
        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully Updated.")
            print()
            input("Enter any key to Continue.")

    def _Delete_Bugs(self):
        try:
            print('-' * 30)
            key = int(
                input("Select one: \n1.Delete Bug's Report \n2.Delete Bug type"))
            print('-' * 30)

            if key == 1:
                bugNo = int(input("Enter bugNo: "))
                qry = f"DELETE From BugReport WHERE bugNo = {bugNo}"
            elif key == 2:
                ob = BugType()
                bugNo = int(input("Enter bugCode: "))
                qry = f"DELETE From BugType WHERE bugCode = {bugNo})"
                cursor.execute(qry)
                con.commit()
            else:
                raise ValueError

        except ValueError:
            print()
            print("Error! Wrong input type.")
            print()
            input("Enter any key to Continue.")
        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully Deleted.")
            print()
            input("Enter any key to Continue.")

# ------------- EMPLOYEE CLASS ---------------


class Employee ():
    def __init__(self, code=None, name=None, email=None, password=None, gender=None, dob=None, mobNo=None, role=None) -> None:
        self._code = code
        self._name = name
        self._email = email
        self._password = password
        self._gender = gender
        self._dob = dob
        self._mobNo = mobNo
        self._role = role

    def detailInput(self):
        try:
            self._code = int(input("Enter empCode: "))
            self._name = input('Enter your Name: ')
            self._email = input('Enter your E-mail: ')
            self._password = input('Enter your Password: ')
            self._gender = input('Enter your Gender: ')
            self._dob = input('Enter your DOB: ')
            self._mobNo = int(input('Enter your mobNo: '))

            print('-' * 30)
            key = int(input("Select Role of Employee: \n \t1. Developer \n \t2. Tester\n"))
            print('-' * 30)

            if key == 1:
                self._role = 'Developer'
            elif key == 2:
                self._role = 'Tester'
            else:
                raise ValueError

            if self._code == None or self._name == '' or self._email == '' or self._password == '' or self._gender == '' or self._dob == '' or self._mobNo == None or self.role == None:
                raise ValueError

        except ValueError:
            print()
            print("Error! Wrong input.")
            print()
            input("Enter any key to Continue.")

    def _display(self):
        print('-' * 12, 'MENU', '-' * 12)
        print('''1. Update Profile
2. Add Bug's Report
3. Update Bug status 
4. View Bug's
5. Bug Detail\’s
6. Exit ''')
        print('-' * 30)

    def _Update_Profile(self):
        try:
            ob = Employee()
            ob.detailInput()

            if self._code == ob._code:
                qry = f"UPDATE Employee SET empName = '{ob._name}', empEmail = '{ob._email}', empPassword = '{ob._password}', gender = '{ob._gender}', DOB = '{ob._dob}', mobileNo = {ob._mobNo}, Role = '{ob._role}' WHERE empCode = {ob._code}"
                cursor.execute(qry)
                con.commit()
            else:
                print("You entered the wrong empCode...")
                return

        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully updated.")
            print()
            input("Enter any key to Continue.")

    def _Add_Bugs_Report(self):
        try:
            ob = BugReport()
            ob.detailInput()

            qry = f"INSERT INTO BugType Values({ob._bugNo}, {ob._bugCode}, {ob._projectID}, {ob._TCode}, {ob._ECode}, '{ob._status}', '{ob._bugDes}')"
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

    def _Update_Bug_Status():
        try:
            ob = BugReport()
            ob._bugNo = int(input('Enter the bugNo: '))

            print('-' * 30)
            key = int(
                input('''Select status of Project: \n \t1. Pending \n \t2. Resolved'''))
            print('-' * 30)

            if key == 1:
                ob._status = 'Pending'
            elif key == 2:
                ob._status = 'Resolved'
            else:
                raise ValueError

            qry = f"UPDATE BugReport SET status = '{ob._status}' WHERE bugNo = {ob._bugNo}"
            cursor.execute(qry)
            con.commit()

        except ValueError:
            print()
            print("Error! Wrong input.")
            print()
            input("Enter any key to Continue.")
        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            print("Successfully updated.")
            print()
            input("Enter any key to Continue.")

    def _View_Bugs():
        try:
            qry = "Select* from BugType"
            cursor.execute(qry)
            result = cursor.fetchall()

        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            display_table(result, 'BugType')
            print()
            input("Enter any key to Continue.")

    def _Bug_Details():
        try:
            print('-' * 30)
            key = int(input('''1. View All \n 2. View by bugCode'''))
            print('-' * 30)
            qry = ''
            if key == 1:
                qry += f"select* from BugReport ORDER BY bugNo ASC"
            elif key == 2:
                id = int(input('Enter bugCode: '))
                qry += f"select* from BugReport where bugCode = {id}"
            else:
                raise ValueError

            cursor.execute(qry)
            result = cursor.fetchall()

        except ValueError:
            print()
            print("Error! Wrong input.")
            print()
            input("Enter any key to Continue.")
        except sql.Error as error:
            print()
            print('Error occurred - ', error)
            print()
            input("Enter any key to Continue.")
        else:
            print()
            display_table(result, 'BugReport')
            print()
            input("Enter any key to Continue.")

# ------------- PROJECT CLASS ---------------


class Project():
    def __init__(self, projectID=None, projectName=None, SDate=None, EDate=None, projectDec=None) -> None:
        self._projectID = projectID
        self._projectName = projectName
        self._SDate = SDate
        self._EDate = EDate
        self._projectDec = projectDec

    def detailInput(self):
        try:
            self._projectID = int(input("Enter projectID: "))
            self._projectName = input('Enter Project Name: ')
            self._SDate = input('Enter Start Date: ')
            self._EDate = input('Enter End Date: ')
            self._projectDec = input('Enter Project Description: ')

            if self._projectID == None or self._projectName == '' or self._SDate == '' or self._EDate == '':
                raise ValueError

        except ValueError:
            print("Error! Wrong input.")

# ------------- BUG_REPORT CLASS ---------------


class BugReport:
    def __init__(self, bugNo=None, bugCode=None, projectID=None, TCode=None, ECode=None, status=None, bugDes=None) -> None:
        self._bugNo = bugNo
        self._bugCode = bugCode
        self._projectID = projectID
        self._TCode = TCode
        self._ECode = ECode
        self._status = status
        self._bugDes = bugDes

    def detailInput(self):
        try:
            self._bugNo = int(input("Enter bugNo: "))
            self._bugCode = int(input('Enter bugCode: '))
            self._projectID = int(input('Enter projectID: '))
            self._TCode = int(input('Enter TCode: '))
            self._ECode = int(input('Enter ECode: '))
            self._bugDes = input('Enter Description of bug: ')
            self._status = 'Pending'

            if self._bugNo == None or self._bugCode == None or self._projectID == None:
                raise ValueError

        except ValueError:
            print("Error! Wrong input.")

# ------------- BUG_TYPE CLASS ---------------


class BugType():
    def __init__(self, bugCode=None, bugCatgory=None, bugSeverty=None) -> None:
        self._bugCode = bugCode
        self._bugCatgory = bugCatgory
        self._bugSeverty = bugSeverty

    def detailInput(self):
        try:
            self._bugCode = int(input("Enter bugCode: "))
            self._bugCatgory = input("Enter bug Category: ")
            print('-' * 30)
            key = int(input(
                '''Select Severty level of Bug: \n \t1. Critical \n \t2. Major \n \t3. Medium \n \t4. Low'''))
            print('-' * 30)

            if key == 1:
                self._bugSeverty = 'Critical'
            elif key == 2:
                self._bugSeverty = 'Major'
            elif key == 3:
                self._bugSeverty = 'Medium'
            elif key == 4:
                self._bugSeverty = 'Low'
            else:
                raise ValueError

            if self._bugCode == None or self._bugCatgory == '' or self._bugSeverty == '':
                raise ValueError

        except ValueError:
            print()
            print("Error! Wrong input.")
            print()
            input("Enter any key to Continue.")


def logIn():
    try:
        print('-' * 11, 'Log In', '-' * 11)
        userId = int(input('Enter your Username(empCode): '))
        password = input('Enter password: ')
        print('-' * 30)

        qry = f"select* from Employee where empCode == '{userId}' and empPassword == '{password}'"
        cursor.execute(qry)
        result = cursor.fetchone()

    except ValueError:
        print()
        print("Error! Wrong input.")
        print()
        input("Enter any key to Continue.")
    except sql.Error as error:
        print()
        print('Error occurred - ', error)
        print()
        input("Enter any key to Continue.")
    else:
        if len(result) > 0:
            return result
        else:
            print()
            print("Something went wrong...")
            print()
            input("Enter any key to Continue.")


def conClose():
    try:
        if con:
            cursor.close()
            con.close()
            print("The BTS connection is closed")
    except sql.Error as error:
        print()
        print('Error occurred - ', error)
        print()
        input("Enter any key to Continue.")
