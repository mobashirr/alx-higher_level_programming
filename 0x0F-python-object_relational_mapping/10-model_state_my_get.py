#!/usr/bin/python3

''' print desired state id'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: ./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>")
        return

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine and connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()

    # Query the database for the state with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
