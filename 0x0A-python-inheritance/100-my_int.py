#!/usr/bin/python3
"""
Module 100-my_int
It contains class MyInt that inherits from int
Sneaky --> has == and != operators inverted!
"""


class MyInt(int):
    """
    Methods:
        __init__(self, num)
        __eq__(self, other)
        __ne__(self, other)
    """
    def __init__(self, num):
        """initialize num"""
        self.num = num

    def __eq__(self, other):
        """
        Return:
           True if both are not equal
        """
        return self.num != other

    def __ne__(self, other):
        """
        Return:
           True if both are equal
        """
        return self.num == other
