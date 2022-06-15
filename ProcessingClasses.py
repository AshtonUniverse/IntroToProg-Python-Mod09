# ---------------------------------------------------------- #
# Title: Assignment 09 - ProcessingClasses.py
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ALarkin,6.14.2022,Modified code to complete assignment 9
# ---------------------------------------------------------- #

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")
else:
    import DataClasses as DC


class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ALarkin,6.14.2022,Modified class to complete assignment 9
    """

    @staticmethod
    def read_data_from_file(file_name: str):
        """Reads data from a file into a list of dictionary rows:

         :param file_name: (string) with name of file:
         :return: (list) of object rows
        """
        list_of_rows = []
        try:
            import os.path
            isfile_bln = (os.path.isfile(file_name))
            if (isfile_bln == True):
                file = open(file_name, "r")
                for line in file:
                    data = line.split(",")
                    row = DC.Employee(int(data[0]), (data[1]), (data[2]))
                    list_of_rows.append(row)
                file.close()
        except FileNotFoundError as e:
            print("Error file not found:", e, sep='\n')
        except Exception as e:
            print()
            print("Error reading data from file:", e, sep='\n')
        return list_of_rows

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """Writes data from a list of dictionary rows to a file:

        :param file_name: (string) with name of file:
        :param list_of_objects: (list) you want filled with file data:
        :return: status_bln (boolean) return status
        """
        save_bln = False
        try:
            strOverwrite = str(input("Overwrite: " + file_name + "?" + " [y/n] ").strip().lower())
            if (strOverwrite == 'y'):
                file = open(file_name, "w")
                for row in list_of_objects:
                    file.write(row.to_string() + "\n")
                    # file.write(row.__str__() + "\n")
                file.close()
                save_bln = True
                print()  # Add an extra line for looks
                print("*************")
                print("Data Saved")
                print("*************")
            else:
                print("Overwrite = No | File not overwritten")
        except Exception as e:
            print()  # adding a new line for looks
            print("Error saving data:", e, sep='\n')
        return save_bln
