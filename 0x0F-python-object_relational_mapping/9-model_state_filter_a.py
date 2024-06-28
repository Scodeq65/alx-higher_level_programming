#!/usr/bin/python3
""" script that lists all State objects that contain the letter a''
from the database hbtn_0e_6_usa
"""

from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
