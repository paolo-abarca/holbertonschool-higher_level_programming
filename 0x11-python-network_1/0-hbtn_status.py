#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        readpage = response.read()

    content = str(readpage).split("\'")

    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(readpage), readpage, content[1]))
