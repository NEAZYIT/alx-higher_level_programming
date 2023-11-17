#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
It is safe from MySQL injections.
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
    cur.execute("SELECT cities.name FROM cities\
                 JOIN states ON cities.state_id = states.id\
                 WHERE states.name = %s\
                 ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    # Close the cursor and the database connection
    cur.close()
    db.close()
