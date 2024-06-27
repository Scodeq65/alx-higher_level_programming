#!/usr/bin/python3
""" script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities():
    """Connects to a MySQL database and list all cities given."""
    username, password, db_name, state_name = sys.argv[1:5]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = conn.cursor()

    query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER By cities.id ASC
    """
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    print(",".join([row[1] for row in rows]))

    cur.close()
    conn.close()


if __name__ == "__main__":
    list_cities()
