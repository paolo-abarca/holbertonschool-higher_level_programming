#!/usr/bin/python3
"""
Python script that takes a URL and an email address,
sends a POST request to the passed URL with email
as a parameter, and finally returns the response body
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
