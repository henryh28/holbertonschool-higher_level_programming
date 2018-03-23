#!/usr/bin/python3

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker()
    section1_db = Session(bind=engine)

    section1_db.add(State(name="Louisiana"))
    section1_db.commit()

    for result in section1_db.query(State.id).filter_by(
            name="Louisiana").first():
        print(result)

    section1_db.close()
