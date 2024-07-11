#!/usr/bin/python3

import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    
    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the rows returned by the query
    states = cursor.fetchall()
    
    # Loop through the rows and print each state
    for state in states:
        print(state)
    
    # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # List all states
    list_states(username, password, database)
