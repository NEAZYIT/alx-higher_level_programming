#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object. It allows us to execute SQL commands through
    # the same database connection.
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                 JOIN states ON cities.state_id = states.id\
                 ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close the cursor and the database connection
    cur.close()
    db.close()
