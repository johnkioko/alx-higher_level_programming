#!/usr/bin/python3
"""Module for class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of Rectangle class"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints rectangle repr with # in stdout"""

        for line in range(self.__y):
            print("")
        for row in range(self.__height):
            for begin in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """An update of str method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """Takes in multiple arguments and updates attributes
        Args:
            *args: multiple arguments
            **kwargs: dictionary arguments
        """

        attrs = ["id", "width", "height", "x", "y"]
        for elem in range(len(args)):
            for attr in range(len(attrs)):
                if attr == elem:
                    setattr(self, attrs[attr], args[elem])
                    break

        if not args or len(args) == 0:
            for key, val in kwargs.items():
                for attr in range(len(attrs)):
                    if key == attrs[attr]:
                        setattr(self, attrs[attr], val)
                        break

    def to_dictionary(self):
        """Dictionary repr of a rectangle"""

        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
