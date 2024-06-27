#!/usr/bin/python3
"""
0-select_states.py - A script that lists all
states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def list_states():
    """
    Connects to a MySQL database and lists all states
    sorted by id in ascending order.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        connection = MySQLdb.connect(
                host="127.0.0.1",
                port=3306,
                user=username,
                passwd=password,
                db=db_name
        )
        cur = connection.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC LIMIT 5")
        rows = cur.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if cur:
            cur.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    list_states()
