#!/usr/bin/python3
"""
 function to read file
"""


def read_file(filename=""):
    """ use the utf-8 encoding """
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        print(data, end="")
