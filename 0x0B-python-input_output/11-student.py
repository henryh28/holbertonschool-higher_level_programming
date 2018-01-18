#!/usr/bin/python3
"""
Module content
11-student   - Create a 'Student' class with public attributes and methods
"""


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return dictionary content of this Student object """
        return (self.__dict__)
