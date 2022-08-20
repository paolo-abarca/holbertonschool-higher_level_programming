#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your ID
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))

    if r.status_code >= 400:
        print("None")

    else:
        print(r.json().get('id'))
