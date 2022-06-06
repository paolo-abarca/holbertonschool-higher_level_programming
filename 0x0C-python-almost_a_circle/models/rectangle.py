#!/usr/bin/python3
"""
Write the class Rectangle
that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Th class Rectangle that inherits
    from class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of arguments
        the class Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        width private
        instance attributes
        """
        return self.__width

    @property
    def height(self):
        """
        height private
        instance attributes
        """
        return self.__height

    @property
    def x(self):
        """
        x private
        instance attributes
        """
        return self.__x

    @property
    def y(self):
        """
        y private
        instance attributes
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        width set argument
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
        heigth set argument
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """
        x set argument
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """
        y set argument
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        public method def area(self):
        which returns the value of the area of
        the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        public method def display(self):
        which prints to stdout the Rectangle instance
        with the # character
        """
        for a in range(self.__y):
            print()

        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")

            for j in range(self.__width):
                print("#", end="")

            print("")

    def __str__(self):
        """
        __str__ method that returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        public method def update(self, *args):
        which assigns an argument to each attribute
        """
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) > 1:
                self.width = args[1]

            if len(args) > 2:
                self.height = args[2]

            if len(args) > 3:
                self.x = args[3]

            if len(args) > 4:
                self.y = args[4]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value

                if key == "width":
                    self.width = value

                if key == "height":
                    self.height = value

                if key == "x":
                    self.x = value

                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        public method def to_dictionary(self):
        which returns the dictionary representation
        of a Rectangle
        """
        dictionary = {"id": self.id, "width": self.width, "height":
                      self.height, "x": self.x, "y": self.y}
        return dictionary
