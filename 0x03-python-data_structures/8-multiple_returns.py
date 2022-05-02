#!/usr/bin/python3
def multiple_returns(sentence):
    lon = len(sentence)
    first_char = sentence[0]

    if lon == 0:
        return (0, None)
    else:
        _tuple = (lon, first_char)
        return _tuple
