#!/usr/bin/python3

'''this module intract with mysql db using mysqldb module to get the citites in desired state'''

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

        # Create and execute the query using parameterized input to avoid SQL injection
        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cursor.execute(query, (state_name,))

        # Fetch all the results
        rows = cursor.fetchall()

        # Print each city name separated by a comma
        cities = ", ".join([row[0] for row in rows])
        print(cities)

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