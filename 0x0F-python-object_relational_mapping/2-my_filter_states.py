#!/usr/bin/python3

'''this module intract with mysql db using mysqldb module'''

from sys import argv
import MySQLdb


def main():
    ''''main logic'''
    username = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]
    # conect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # Execute the query which pre-formated 
    query = "SELECT id, name FROM states WHERE name = {} ORDER BY id ASC".format(name)
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