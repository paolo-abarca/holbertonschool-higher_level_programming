#!/usr/bin/python3
"""
Python script that takes a URL and an email,
sends a POST request to the passed URL with
the email as a parameter, and returns the
response body (utf-8 decoded)
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("UTF-8"))
