#!/usr/bin/python3
""" Unit Test for 'Base' class """
import unittest
from models.base import Base


class test_base(unittest.TestCase):

    def test_id(self):
        """ Test id attribute """
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base(5)
        self.assertEqual(base2.id, 5)
        base3 = Base()
        self.assertEqual(base3.id, 2)
