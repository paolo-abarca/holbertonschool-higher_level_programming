#!/usr/bin/python3
"""
Adding python script that lists all cities
from hbtn_0e_4_usa database
"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], host='localhost', port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states ON cities.state_id = \
            states.id ORDER BY cities.id;")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
