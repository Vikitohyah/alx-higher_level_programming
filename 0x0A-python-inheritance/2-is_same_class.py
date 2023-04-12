#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList
inherits from list; has public instance method to print sorted list
"""


class MyList(list):
    """inherits from list
    methods:
    print_sorted(self)
    """
    def print_sorted(self):
        """prints list of ints sorted all in ascending order"""
        print(sorted(self))
