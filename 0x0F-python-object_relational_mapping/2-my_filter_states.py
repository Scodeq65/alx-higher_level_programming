#!/usr/bin/python3
"""
2-filter_states.py - A script that lists all states name
that matches the provided arguments from the database.
"""

import MySQLdb
import sys


def filter_states():
    """ Connects to a MySQL database and lists all states
        that matches the provided arguments.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    filter_states()
