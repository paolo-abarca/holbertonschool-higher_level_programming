#!/usr/bin/python3
"""
Write a class Rectangle
(based on 7-base_geometry.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle inherits
    from BaseGeometry
    (7-base_geometry.py)
    """

    def __init__(self, width, height):
        """
        instances initializes
        self, width, height
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """
        str method that returns a message
        """

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        area method that returns the area of a rectangle
        """

        return self.__width * self.__height
