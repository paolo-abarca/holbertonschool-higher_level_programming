#!/usr/bin/python3
"""
Write a function that creates
an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Method that creates an object from a "JSON file"
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        return json.load(myFile)
