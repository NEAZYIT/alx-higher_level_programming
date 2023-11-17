#!/usr/bin/python3
"""
Lists states from hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys


def filter_states():
    # Extracting command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connecting to MySQL database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Creating a cursor object
    cursor = db.cursor()

    # SQL query to select states by name and order by ID
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    data = cursor.fetchall()

    # Displaying the fetched data
    for row in data:
        print(row)

    # Closing cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
