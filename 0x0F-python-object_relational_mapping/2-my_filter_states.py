#!/usr/bin/python3

"""
2-my_filter_states.py - A script that displays all values
in the states table
where name matches the provided state name argument.
"""

import MySQLdb
import sys


def filter_states():
    """
    Connects to a MySQL database and queries the states table
    based on the provided state name argument.
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

    try:
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        cur.execute(query, (state_name,))
        rows = cur.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error querying MySQL: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    filter_states()
