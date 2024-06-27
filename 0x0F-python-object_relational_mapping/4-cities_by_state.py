#!/usr/bin/python3
"""
4-cities_by_state.py - A script that lists all cities
from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def list_cities():
    """
    Connects to a MySQL database and lists all
    cities sorted by id in ascending order.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = conn.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    list_cities()
