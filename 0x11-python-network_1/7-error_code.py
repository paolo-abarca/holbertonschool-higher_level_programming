#!/usr/bin/python3
"""
Python script that takes a URL, sends a request
to the URL, and returns the response body
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))

    else:
        print(r.text)
