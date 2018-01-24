#!/usr/bin/python3
"""
Module content
base.py   - Create a Base class for other classes to inherit from
"""
import json
import csv


class Base:
    """ Base class to inherit from """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization constructor method """

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON representation of 'list_dictionaries'/self """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @staticmethod
    def from_json_string(json_string):
        """ Reconstitute list of representation of objects from JSON """
        return json.loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON representation of 'list_objs' to a file """

        data = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(data))

    @classmethod
    def load_from_file(cls):
        """ Instantiate objects from a file """

        try:
            with open("{}.json".format(cls.__name__), "r",
                      encoding="utf-8") as f:
                data = cls.from_json_string(f.read())
                return ([cls.create(**obj) for obj in data] if data else [])
        except FileNotFoundError:
            return ([])

    @classmethod
    def create(cls, **dictionary):
        """ Instantiate object with supplied values """

        obj = cls(1, 2)
        obj.update(**dictionary)
        return (obj)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Write JSON representation of 'list_objs to a csv file """

        with open("{}.csv".format(cls.__name__), "w", encoding="utf-8") as f:
            for item in list_objs:
                if cls.__name__ == "Rectangle":
                    f.write("{}, {}, {}, {}, {}\n".format(
                        item.id, item.width, item.height, item.x, item.y))
                if cls.__name__ == "Square":
                    f.write("{}, {}, {}, {}\n".format(
                        item.id, item.width, item.x, item.y))

    @classmethod
    def load_from_file_csv(cls):
        """ Instantiate objects from a csv file """

        with open("{}.json".format(cls.__name__), "r", encoding="utf-8") as f:
            data = cls.from_json_string(f.read())
            return ([cls.create(**obj) for obj in data] if data != [] else [])
