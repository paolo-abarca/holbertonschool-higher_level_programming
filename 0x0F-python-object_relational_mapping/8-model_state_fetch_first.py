#!/usr/bin/python3
"""
Adding a Python script that prints the first
State object from the hbtn_0e_6_usa database
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
    states = session.query(State).filter(State.id == 1).order_by(State.id)

    if states is not None:
        for state in states:
            print("{}: {}".format(state.id, state.name))

    else:
        print("Nothing")
