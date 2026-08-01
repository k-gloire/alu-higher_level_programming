#!/usr/bin/python3
"""Lists all cities with their corresponding state names."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )

    session = Session(engine)

    cities = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for city, state in cities:
        print("{}: ({}) {}".format(
            state.name,
            city.id,
            city.name
        ))

    session.close()
