#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    value = 0
    for number in range(1, len(argv)):
        value = value + int(argv[number])
    print("{}".format(value))
