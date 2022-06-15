# ------------------------------------------------------------------------ #
# Title: Assignment 09 - Main.py
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# ALarkin,6.14.2022,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

strFileName = "EmployeeData.txt"
intEmployeeId = 0
strFirstName = ""
strLastName = ""

# TODO: Import Modules
# print (__name__)
if __name__ == "__main__":
    from DataClasses import Employee as EMP
    from ProcessingClasses import FileProcessor as FP
    from IOClasses import EmployeeIO as EIO
    # print("This file is the starting point of my program!")
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# TODO: Load data from file into a list of employee objects when script starts
lstOfEmployeeObjects = FP.read_data_from_file(strFileName)

while (True):
    # TODO: Show user a menu of options
    EIO.menu()  # Shows menu
    # TODO: Get user's menu option choice
    strChoice = EIO.choice()
    # TODO: Show user current data in the list of employee objects
    if strChoice.strip() == '1':
        EIO.employee_list(lstOfEmployeeObjects)  # Show current data in the list/table
        continue
    # TODO: Add data to the list of employee objects
    elif strChoice.strip() == '2':
        intEmployeeId, strFirstName, strLastName = EIO.input_employee_data()
        if not (intEmployeeId == 0 or strFirstName == "" or strLastName == ""):
            lstOfEmployeeObjects.append(EMP(employee_id=intEmployeeId,
                                            first_name=strFirstName,
                                            last_name=strLastName))
        else:
            continue
    # Added option to remove data from the list of employee objects
    elif strChoice.strip() == '3':
        EIO.remove_data(lstOfEmployeeObjects)
        continue
    # TODO: Save current data to file
    elif strChoice == '4':
        FP.save_data_to_file(strFileName, lstOfEmployeeObjects)
        continue
    # TODO: Exit program
    elif strChoice == '5':
        break

# Exit the program
input("\nPress the enter key to exit.")

# Main Body of Script  ---------------------------------------------------- #
