#!/usr/bin/python3
"""
0-select_states.py - Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states():
    """ Alternative testing code. """
    username, password, db_name = sys.argv[1:4]
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_states()
