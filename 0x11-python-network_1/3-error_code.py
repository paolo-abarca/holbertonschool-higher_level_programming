#!/usr/bin/python3
"""
Python script that takes a URL, sends a request to the URL,
and returns the response body (utf-8 decoded)
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("UTF-8"))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
