#!/usr/bin/python3
"""
Write a class Student
that defines a student by
"""


class Student:
    """
    The class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        initializes arguments
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return representation
        """

        return self.__dict__
