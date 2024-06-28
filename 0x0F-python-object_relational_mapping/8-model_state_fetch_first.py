#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

def fetch_first_state():
    """Fetches the first State object from the database."""
    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine that connects to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}', pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the first State object
    state = session.query(State).order_by(State.id).first()

    # Display the result
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()

if __name__ == "__main__":
    fetch_first_state()
