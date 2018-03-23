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

    hit = section1_db.query(State).first()
    print("{}: {}".format(hit.id, hit.name)) if hit else print("Nothing")

    section1_db.close()
