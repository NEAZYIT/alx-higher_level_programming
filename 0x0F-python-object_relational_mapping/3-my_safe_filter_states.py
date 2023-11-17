#!/usr/bin/python3
"""
This script accepts an argument and displays all matching values in the states
table of hbtn_0e_0_usa where the name matches the argument. It is safe from
MySQL injections.
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
    cur.execute("SELECT * FROM states WHERE name = %s\
                 ORDER BY id ASC", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close the cursor and the database connection
    cur.close()
    db.close()
