#!/usr/bin/python3

'''Module for Student class.'''


class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of a Student instance"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))