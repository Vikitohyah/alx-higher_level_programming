#!/usr/bin/python3
"""
Module 4-inherits_from.py
It contains method inherits_from
And returns True if obj is instance of class that it inherits from or is subcls of
"""


def inherits_from(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and parent classes as well
        use issubclass() to get what object is a subclass
    Return:
        True if obj is instance of class that it inherits from or is subcls of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
