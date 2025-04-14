import Bug_Tracking_System as Bts
import sys
try:
    result = Bts.logIn()

    if result[7] == 'Admin':
        ob = Bts.Admin(result[0], result[1], result[2],
                    result[3], result[4], result[5], result[6])

        while True:
            ob._display()
            key = int(input('\n'))

            if key == 1:
                while True:
                    ob._Manager()
                    key2 = int(input('\n'))

                    if key2 == 1:
                        ob._Add_Manager_Account()
                    elif key2 == 2:
                        ob._View_Manager_Account()
                    elif key2 == 3:
                        ob._Delete_Manager()
                    elif key2 == 4:
                        ob._Update_Manager_Details()
                    elif key2 == 5:
                        break

            elif key == 2:
                while True:
                    ob._Employee()
                    key2 = int(input('\n'))

                    if key2 == 1:
                        ob._Add_Employee_Account()
                    elif key2 == 2:
                        ob._View_Employees_Account()
                    elif key2 == 3:
                        ob._Delete_Employee_Account()
                    elif key2 == 4:
                        ob._Update_Employee_Details()
                    elif key2 == 5:
                        break

            elif key == 3:
                ob._View_All_Project()
            elif key == 4:
                ob._View_Bugs_Reports()
            elif key == 5:
                sys.exit()

    elif result[7] == 'Manager':
        ob = Bts.Manager(result[0], result[1], result[2],
                        result[3], result[4], result[5], result[6])

        while True:
            ob._display()
            key = int(input('\n'))

            if key == 1:
                ob._Update_Profile()
            elif key == 2:
                ob._Manage_Project()
                key2 = int(input('\n'))

                if key2 == 1:
                    ob._Add_Project()
                elif key2 == 2:
                    ob._View_All_Projects()
                elif key2 == 3:
                    ob._Delete_Project()
                elif key2 == 4:
                    ob._Update_Project()

            elif key == 3:
                ob._bug_Display()
                key2 = int(input('\n'))

                if key2 == 1:
                    ob._Add_New_Bug()
                elif key2 == 2:
                    ob._View_All_Bugs()
                elif key2 == 3:
                    ob._Update_Bug()
                elif key2 == 4:
                    ob._Delete_Bugs()
            elif key == 4:
                sys.exit()

    else:
        ob = Bts.Employee(result[0], result[1], result[2], result[3],
                        result[4], result[5], result[6], result[7])

        while True:
            ob._display()
            key = int(input('\n'))

            if key == 1:
                ob._Update_Profile()
            elif key == 2:
                ob._Add_Bugs_Report()
            elif key == 3:
                ob._Update_Bug_Status()
            elif key == 4:
                ob._View_Bugs()
            elif key == 5:
                ob._Bug_Details()
            elif key == 6:
                sys.exit()

except ValueError:
    print('Error! Invalid input.')
except:
    print('Unexpected error!')
finally:
    Bts.conClose()
    sys.exit()