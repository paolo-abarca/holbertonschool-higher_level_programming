#!/usr/bin/python3
"""
Adding a Python script that prints the State
object with the name passed as an argument
from the hbtn_0e_6_usa database
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
    states = session.query(State).filter(State.name == argv[4]).first()

    if states is not None:
        print(states.id)

    else:
        print("Not found")
