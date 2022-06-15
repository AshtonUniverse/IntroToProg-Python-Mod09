# ---------------------------------------------------------- #
# Title: Assignment 09 - TestHarness.py
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ALarkin,6.14.2022,Update script
# ---------------------------------------------------------- #

if __name__ == "__main__":
    from DataClasses import Employee as EMP
    from ProcessingClasses import FileProcessor as FP
    from IOClasses import EmployeeIO as EIO
else:
    raise Exception("This file was not created to be imported")

# Test data module: [DataClasses.py]
print()
print("Test data module: [DataClasses.py]")
print("**************************************************")
print()
p1 = EMP(1, "Haruka", "Nanase")
p2 = EMP(2, "Makoto", "Tachibana")
p3 = EMP(3, "Nagisa", "Hazuki")
p4 = EMP(4, "Rin", "Matsuoka")
lstTable = [p1, p2, p3, p4]
for row in lstTable:
    print(row.to_string(), type(row))
print()

# Test processing module: [ProcessingClasses.py]
print("Test processing module: [ProcessingClasses.py]")
print("**************************************************")
print()
print("[save_data_to_file:]")
print()
FP.save_data_to_file("EmployeeData.txt", lstTable)
print()
print("[read_data_from_file:]")
print()
lstFileData = FP.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for row in lstFileData:
    lstTable.append(row)
for row in lstTable:
    print(row.to_string(), type(row))
print()

# Test IO module: [IOClasses.py]
print("Test IO module: [IOClasses.py]")
print("**************************************************")
print()
print("[menu:]")
print()
EIO.menu()
print()
print("[employee_list:]")
print()
EIO.employee_list(lstTable)
print()
print("[choice:]")
print()
print(EIO.choice())
print()
print("[input_employee_data:]")
print()
print(EIO.input_employee_data()) # (9, 'TestFirst', 'TestLast')
print()
print("[remove_data:]")
print()
print(EIO.remove_employee_data(lstTable)) # (9, 'TestFirst', 'TestLast')
print()
