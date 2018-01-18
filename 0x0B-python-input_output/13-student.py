#!/usr/bin/python3
"""
Module content
13-student   - Create a 'Student' class with public attributes and methods
"""


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, argv=None):
        """ Return dictionary content of this Student object """
        if argv is None:
            return (self.__dict__)

        kv = {}
        for key in argv:
            if key in (self.__dict__):
                kv[key] = self.__dict__[key]
        return (kv)

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = value
