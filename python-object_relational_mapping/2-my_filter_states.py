#!/usr/bin/python3
"""Filter states script.

Lists all values in the states table where name matches the
argument, using format() to build the query (case sensitive).
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}'".format(search)
    query += " ORDER BY id ASC"
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
