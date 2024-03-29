#!/usr/bin/python3
"""
The lookup function container
"""


def lookup(obj):
    """
    Args:
        obj: initial object
        Returns: a list of available features and
                 methods of an object
    """
    return dir(obj)
