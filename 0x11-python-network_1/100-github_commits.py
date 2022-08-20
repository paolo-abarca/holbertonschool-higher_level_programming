#!/usr/bin/python3
"""
python script that takes 2 arguments to solve this challenge
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(argv[1], argv[2]))

    if r.status_code >= 400:
        print("None")

    else:
        fjson = r.json()
        for i in range(10):
            print("{}: {}".format(fjson[i].get('sha'),
                                  fjson[i].get('commit').get('author')
                                  .get('name')))
