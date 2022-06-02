#!/usr/bin/python3
"""
Write a class LockedClass with no
class or object attribute
"""


class LockedClass:
    """
    the class LockedClass
    """
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """
        initialized arguments
        """
        self.first_name = first_name
