#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list = new_list + [True]
            continue
        else:
            new_list = new_list + [False]
            continue

    return new_list
