#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upper = chr(ord(i) - 32)
            print("{:s}".format(upper), end="")
        else:
            print("{}".format(i), end="")
    print()
