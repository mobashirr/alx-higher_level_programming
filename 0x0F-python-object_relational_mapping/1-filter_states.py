#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        # Get command line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Connect to the database
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute the query with filter
        cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        # Fetch all the results
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
