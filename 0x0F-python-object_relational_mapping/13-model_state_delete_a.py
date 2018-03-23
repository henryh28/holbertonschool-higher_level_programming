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

    for entry in section1_db.query(State).all():
        if "a" in entry.name:
            section1_db.delete(entry)

    section1_db.commit()
    section1_db.close()
