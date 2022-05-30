#!/usr/bin/python3
"""
Write a class MyList
that inherits from list
"""


class MyList(list):
    """
    The MyList class that
    inherits from the list
    """

    def print_sorted(self):
        """
        method that prints
        a new ordered list
        """
        new_list = sorted(self)
        print("{}".format(new_list))
