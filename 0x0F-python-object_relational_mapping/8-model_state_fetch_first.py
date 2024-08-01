#!/usr/bin/python3

"""Print the first State object from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./<script_name> <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)
    
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the database engine
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{database}', pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()

    # Query the first State object ordered by id
    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
