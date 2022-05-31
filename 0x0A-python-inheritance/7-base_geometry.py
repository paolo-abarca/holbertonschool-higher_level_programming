#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 5-base_geometry.py)
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        area method that prints an exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator method that prints an exception message
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
