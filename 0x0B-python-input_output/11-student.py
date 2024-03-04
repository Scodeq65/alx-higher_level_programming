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

    def to_json(self, attrs=None):
        """Retrives a dict representation of a student instance
        Args:
            attrs (list): List of atttributes of names to retrive.
            Default is None
        Returns:
            dict: A dictionary representation of the student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs
                    if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """Replaces all attributes of student instances.
        Args:
            json (dict): Dictionary coataining attribute
            names and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)
