#!/usr/bin/python3

'''Module for Student class.'''


class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
