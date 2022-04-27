#!/usr/bin/python3
for letter in range(122, 97-1, -2):
    print("{:c}{:s}".format(letter, chr(letter-33)), end="")
