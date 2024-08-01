#!/usr/bin/python3

'''this module intract with sqlalchemy module to establish connection to mysql server and query data'''

from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # create engine to establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states from the database
    states = session.query(State).order_by(State.id).all()

    # Print each state in the required format
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if len(sys.argv) > 3:
    main()
else:
    print(f"USAGE {sys.argv[0]} mysql_username mysql_password  database_name")