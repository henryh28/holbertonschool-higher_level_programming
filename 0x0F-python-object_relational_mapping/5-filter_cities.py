#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    comma = 0
    for state in cursor.fetchall():
        if state[1] == argv[4]:
            comma = 1 if comma == 0 else print(", ", end="")
            print(state[0], end="")

    if comma != 0:
        print()
    cursor.close()
    db.close()
