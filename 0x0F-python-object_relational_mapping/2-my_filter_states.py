#!/usr/bin/python3

'''this module intract with mysql db using mysqldb module'''

import sys
import MySQLdb


def main():
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Create the query using format
        query = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
        cursor.execute(query)

        # Fetch all the results
        rows = cursor.fetchall()

        # Print each rowa
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


if len(sys.argv) > 4:
    main()
else:
    print(f"USAGE {sys.argv[0]} mysql_username mysql_password  database_name")