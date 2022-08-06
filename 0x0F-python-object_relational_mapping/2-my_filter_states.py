#!/usr/bin/python3
"""
Adding a python script that takes an argument
and displays all values in the state table of
hbtn_0e_0_usa where the name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], host='localhost', port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name \
            LIKE BINARY '" + argv[4] + "' ORDER BY states.id")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
