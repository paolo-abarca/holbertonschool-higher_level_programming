#!/usr/bin/python3
"""
Adding a python script that takes a state name
as an argument and lists all the cities in that state,
using the hbtn_0e_4_usa database
"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], host='localhost', port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities INNER JOIN \
            states ON cities.state_id = states.id WHERE \
            states.name=%s ORDER BY cities.id;", (argv[4],))

    rows = cursor.fetchall()

    value = []
    for row in rows:
        value.append(row[0])

    print(", ".join(value))

    cursor.close()
    db.close()
