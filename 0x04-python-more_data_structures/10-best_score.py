#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        Key_max = max(a_dictionary.keys())
        return Key_max
    else:
        return None
