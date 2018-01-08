#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7]), 7)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_strings(self):
        self.assertEqual(max_integer("string"), 't')

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 3.4, 5.6]), 5.6)

    def test_no_input(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_integer((4.5, "bob", 7.2))

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, -5.7, 0, 3, 40.17]), 40.17)


if __name__ == '__main__':
    unittest.main()
