#!/usr/bin/python3

'''task 12'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>")
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

    # Query the database for the state with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Check if the state exists and update its name
    if state:
        state.name = 'New Mexico'
        session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
