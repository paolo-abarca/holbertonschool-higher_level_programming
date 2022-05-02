#!/usr/bin/python3
def multiple_returns(sentence):
    lon = len(sentence)

    if lon == 0:
        return (0, None)
    else:
        first_char = sentence[0]
        _tuple = (lon, first_char)
        return _tuple
