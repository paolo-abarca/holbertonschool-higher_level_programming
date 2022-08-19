#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found
in the header of the response
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen('https://intranet.hbtn.io') as response:
        value = response.headers["X-Request-Id"]

    print(value)
