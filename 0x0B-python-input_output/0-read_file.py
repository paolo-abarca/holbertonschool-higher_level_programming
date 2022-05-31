#!/usr/bin/python3
"""
Write a function that reads
a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    method that reads and prints text files
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
