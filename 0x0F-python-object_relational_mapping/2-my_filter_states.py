#!/usr/bin/python3
"""
2-my_filter_states.py - A script that displays all values
in the states table where name matches the provided argument.
"""

import MySQLdb
import sys


def filter_states():
    """Connects to a MySQL database and queries the states table
    based on the provided state anme argument.
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

    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY id ASC".format(state_name)
    )

    cur.execute(query)

    rows = cur.fetchall()

    unique_rows = set(rows)
    for row in unique_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    filter_states()
