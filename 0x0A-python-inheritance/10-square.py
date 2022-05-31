#!/usr/bin/python3
"""
Write a class Square
(based on 9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square inherits
    from Rectangle
    (9-rectangle.py)
    """

    def __init__(self, size):
        """
        instances initializes
        self, size
        """

        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """
        str method that returns a message
        """

        return str("[Rectangle] {}/{}".format(self.__size, self.__size))

    def area(self):
        """
        area method that returns the area of a square
        """

        return self.__size ** 2
