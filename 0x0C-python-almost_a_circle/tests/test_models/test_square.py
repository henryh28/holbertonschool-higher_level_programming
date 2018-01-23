#!/usr/bin/python3
""" Unit Test for 'Square' class """
import unittest
import sys
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class test_base(unittest.TestCase):

    def test_parent(self):
        """ Test for parent class value """
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_instantiate(self):
        """ Test instantiation """
        with (self.assertRaises(TypeError)):
            square1 = Square()

        square2 = Square(3)
        self.assertEqual(square2.width, 3)
        self.assertEqual(square2.height, 3)
        self.assertEqual(square2.x, 0)
        self.assertEqual(square2.y, 0)

        square3 = Square(4, 5, 6, 199)
        self.assertEqual(square3.width, 4)
        self.assertEqual(square3.height, 4)
        self.assertEqual(square3.x, 5)
        self.assertEqual(square3.y, 6)
        self.assertEqual(square3.id, 199)

    def test_errors(self):
        """ Test for error triggers """
        with (self.assertRaises(TypeError)):
            square4 = Square("1")
        with (self.assertRaises(TypeError)):
            square4 = Square([4])
        with (self.assertRaises(ValueError)):
            square4 = Square(0)
        with (self.assertRaises(ValueError)):
            square4 = Square(1, 0, -1)
        with (self.assertRaises(ValueError)):
            square4 = Square(1, -10, 10)

    def test_update(self):
        """ Test for updating attributes """
        square5 = Square(8)
        self.assertEqual(square5.width, 8)
        self.assertEqual(square5.height, 8)

        square5.size = 6
        self.assertEqual(square5.width, 6)
        self.assertEqual(square5.height, 6)

        square5.update(40, 30, 20, 10)
        self.assertEqual(square5.id, 40)
        self.assertEqual(square5.width, 30)
        self.assertEqual(square5.height, 30)
        self.assertEqual(square5.x, 20)
        self.assertEqual(square5.y, 10)

        square5.update(x=41, id=31, size=21, y=11)
        self.assertEqual(square5.id, 31)
        self.assertEqual(square5.width, 21)
        self.assertEqual(square5.height, 21)
        self.assertEqual(square5.x, 41)
        self.assertEqual(square5.y, 11)
