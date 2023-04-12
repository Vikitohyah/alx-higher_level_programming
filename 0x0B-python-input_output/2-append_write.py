#!/usr/bin/python3
"""append write to a file"""


def append_write(filename="", text=""):
    """"append write to a file"""
    with open(filename, mode="a", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)
