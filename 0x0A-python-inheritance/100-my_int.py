#!/usr/bin/python3
"""
Module content
100-my_int - Create a MyInt class that inherits from int, flip == and !=
"""


class MyInt(int):

    # Reference http://thepythonguru.com/python-operator-overloading/
    def __eq__(self, other):
        """ Overrides == operator to give != results """
        return (not super().__eq__(other))

    def __ne__(self, other):
        """ Overrides != operator to give == results """
        return (not super().__ne__(other))
