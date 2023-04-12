#!/usr/bin/python3
"""
Module 10-square
It contains the parent class BaseGeometry
with public instance method area and integer_validation
It contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent,
extends parent's area method and prints with __str__
It contains subclass Square
with instantiation of private attribute size, validated by superclass,
and prints with __str__
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, which in turn inherits from BaseGeometry
    methods:
        __init__(self, size)
        __str__(self)
    """
    def __init__(self, size):
        """initializes size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)

