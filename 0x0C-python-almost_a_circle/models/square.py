#!/usr/bin/python3
"""
Write the class Square
that inherits from Rectangle
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Th class Square that inherits
    from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of arguments
        the class Square
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        __str__ method should return
        [Square] (<id>) <x>/<y> - <size> -
        in our case width or height
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.__width))

    @property
    def size(self):
        """
        size private
        instance attributes
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        size set argument
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        public method def update(self, *args, **kwargs)
        that assigns attributes
        """
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) > 1:
                self.size = args[1]

            if len(args) > 2:
                self.x = args[2]

            if len(args) > 3:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value

                if key == "size":
                    self.size = value

                if key == "x":
                    self.x = value

                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        public method def to_dictionary(self):
        which returns the dictionary
        representation of a Square
        """
        dictionary = {"id": self.id, "size": self.size,
                      "x": self.x, "y": self.y}
        return dictionary
