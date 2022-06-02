#!/usr/bin/python3
def magic_string(text=[0]):
    text[0] += 1
    return str("BestSchool, " * (text[0] - 1)) + "BestSchool"
