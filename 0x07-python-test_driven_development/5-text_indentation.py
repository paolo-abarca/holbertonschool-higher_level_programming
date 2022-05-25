#!/usr/bin/python3
"""
Python function
that prints a text
with 2 new lines
"""


def text_indentation(text):
    """
    Prints a text
    with 2 new lines
    """

    characters = [".", "?", ":"]

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in characters:
            print("\n")

            try:
                if text[i + 1] == " ":
                    i += 1
                if text[i + 1] == " ":
                    i += 1
                if text[i + 1] == " ":
                    i += 1
                if text[i + 1] == " ":
                    i += 1
            except IndexError:
                break

        i += 1
