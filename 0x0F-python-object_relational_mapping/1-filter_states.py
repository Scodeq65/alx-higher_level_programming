#!/usr/bin/python3
"""
1-filter_states.py - A script that lists all states name
that starts with 'N' from the database.
"""

import MySQLdb
import sys


def filter_states():
    """ Connects to a MySQL database and lists all states
    starting with 'N' in ascending order.
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = conn.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    filter_states()
