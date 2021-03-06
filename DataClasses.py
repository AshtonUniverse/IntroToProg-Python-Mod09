# ---------------------------------------------------------- #
# Title: Assignment 09 - DataClasses.py
# Description: A module of data classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ALarkin,6.14.2022,Modified code to complete assignment 9
# ---------------------------------------------------------- #

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


class Person(object):  # Inherits from object
    """Stores data about a person:

    properties:
        first_name: (string) person first name

        last_name: (string) person last name
    methods:
        to_string() returns comma separated product data (alias for __str__())
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ALarkin,6.14.2022,Modified class to complete assignment 9
    """

    # -- Constructor --
    def __init__(self, first_name: str, last_name: str):
        # -- Attributes --
        self.__first_name = first_name
        self.__last_name = last_name

    # -- Properties --
    @property
    def first_name(self):
        return str(self.__first_name).strip().lower().title()

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return str(self.__last_name).strip().lower().title()

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    # -- Methods --
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def __str__(self):
        """ Implicitly returns a string with this object's data """
        return self.first_name + ',' + self.last_name


class Employee(Person):  # Inherits from Person
    """Stores data about an employee:

    properties:
        employee_id: (int) employee ID

        first_name: (string) employee first name

        last_name: (string) employee last name
    methods:
        to_string() returns comma separated product data (alias for __str__())
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ALarkin,6.14.2022,Modified class to complete assignment 9
    """

    def __init__(self, employee_id: int, first_name: str, last_name: str):
        # Attributes
        self.__employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name

    # --Properties--
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        self.__last_name = int(value)

    # --Methods--
    def to_string(self):  # Overrides the original method (polymorphic)
        """ Explicitly returns a string with this object's data """
        # Linking to self.__str__() does not work with inheritance
        data = super().__str__()  # get data from parent(super) class
        return str(self.employee_id) + ',' + data

    def __str__(self):  # Overrides the original method (polymorphic)
        """ Implicitly returns field data """
        data = super().__str__()  # get data from parent(super) class
        return str(self.employee_id) + ',' + data
    # --End of Class --
