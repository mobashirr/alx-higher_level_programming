#!/usr/bin/python3

"""Print the first State object from the database where state have a letter"""

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>")
        return

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()

    # Query the database
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
