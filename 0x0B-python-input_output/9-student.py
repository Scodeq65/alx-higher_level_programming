#!/usr/bin/python3
"""Create a new student class."""


class Student:
    """Defines a student by first_name, last_name  and age."""
    def __init__(self, first_name, last_name, age):
        """Initializes the student class with firtname, last name and age.
        Args:
            first_name (str): The student first name
            last_name (str): The student last name
            age (int): The student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives a dict representation of a student instance
        Returns:
            dict: A dictionary representation of the student instance.
        """
        return self.__dict__
