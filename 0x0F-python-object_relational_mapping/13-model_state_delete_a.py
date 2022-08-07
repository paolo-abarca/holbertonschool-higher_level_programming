#!/usr/bin/python3
"""
Adding a Python script that removes all
State objects with a name containing the
letter a from the hbtn_0e_6_usa database
"""


if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        session.delete(state)

    session.commit()
