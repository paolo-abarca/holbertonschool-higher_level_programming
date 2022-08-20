#!/usr/bin/python3
"""
python script that takes 2 arguments to solve this challenge
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])

    r = requests.get(url)

    try:
        fjson = r.json()
        for i in range(10):
            print("{}: {}".format(fjson[i].get('sha'),
                                  fjson[i].get('commit').get('author')
                                  .get('name')))
    except IndexError:
        pass
