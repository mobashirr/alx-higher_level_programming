#!/usr/bin/python3

'''use mysqldb to fetch data from mysql server'''

from sys import argv
import MySQLdb

def main():
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # conect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Create and execute the query
    query = """
    SELECT cities.id, cities.name, states.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the results
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()

if len(argv) > 3:
    main()
else:
    print(f"USAGE {argv[0]} mysql_username mysql_password  database_name")