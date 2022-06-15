# ---------------------------------------------------------- #
# Title: Assignment 09 - IOClasses.py
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ALarkin,6.14.2022,Modified code to complete assignment 9
# ---------------------------------------------------------- #

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


class EmployeeIO:
    """ A class for performing Employee Input and Output

    methods:
        menu():

        choice():

        employee_list(list_of_rows):

        input_employee_data():

        remove_data(lstOfEmployeeObjects):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ALarkin,6.14.2022,Modified class to complete assignment 9
    """

    @staticmethod
    def menu():
        """ Display a menu of options to the user

        :return: nothing
        """
        print('''
        ******************************
        Employee Data - Option Menu
        ******************************
        1) Show current employees
        2) Add a new employee
        3) Remove an employee
        4) Save employee data to file        
        5) Exit program
        ******************************
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def choice():
        """ Get users menu choice

        :return: (str) choice
        """
        choice = str(input("Choose an option? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        if str(choice) not in ("1", "2", "3", "4", "5"):
            print("******************************")
            print(choice + " is not a valid option")
            print("******************************")
            print()  # Add an extra line for looks
        return choice

    @staticmethod
    def employee_list(list_of_rows: list):
        """ Print current employees in the list of rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******** Current Employee List *************")
        for row in list_of_rows:
            print(str(row.employee_id) + "," + row.first_name + "," + row.last_name)
        print("*******************************************")
        print()  # Add an extra line for looks
        return

    @staticmethod
    def input_employee_data():
        """ Get users input data for an employee object

        :return: (int) employee_id, (str) first_name, (str) last_name
        """
        try:
            employee_id = str(input("What is the employee Id? - ").strip())
            first_name = str(input("What is the employee First Name? - ").strip())
            last_name = str(input("What is the employee Last Name? - ").strip())
            print()  # Add an extra line for looks
            if not str(employee_id).isnumeric():
                employee_id = 0
                print("********************************")
                print("Employee ID must be a number!")
            if str(first_name).isnumeric():
                first_name = ""
                print("First Name must not be a number!")
            if str(last_name).isnumeric():
                last_name = ""
                print("Last Name must not be a number!")
                print("********************************")
            return int(employee_id), first_name, last_name
        except Exception as e:
            print("Invalid data entered:", e, sep='\n')
        return

    @staticmethod
    def remove_employee_data(lstOfEmployeeObjects: list):
        """ Remove data for an employee object

        :param lstOfEmployeeObjects
        :return: nothing
        """
        try:
            employee_id = int(input("Enter an employee id to remove: ").strip())
            first_name = ""
            last_name = ""
            remove_bln = False  # verify that the data was found
            for row in lstOfEmployeeObjects:
                if row.employee_id == employee_id:
                    first_name = row.first_name
                    last_name = row.last_name
                    lstOfEmployeeObjects.remove(row)
                    remove_bln = True
            if remove_bln:
                print()  # Add an extra line for looks
                print("***********************************************")
                print(str(first_name + " " + last_name) + " removed from Employee List. ")
                print("***********************************************")
            else:
                print()  # Add an extra line for looks
                print("******************************")
                print(str(employee_id) + " is not a valid Employee ID. ")
                print("******************************")
        except Exception as e:
            print()  # adding a new line for looks
            print("Error Removing Data:", e, sep='\n')
