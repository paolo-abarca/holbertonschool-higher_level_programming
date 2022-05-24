#!/usr/bin/python3
"""Unittest for function max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the function max_integer"""

    def not_integer(self):
        """Test for the function max_integer"""
        result = max_integer([])
        self.assertEqual(result, None)

    def none_integer(self):
        """Test for the function max_integer"""
        result = max_integer([])
        self.assertEqual(result, None)

    def zero_integer(self):
        """Test for the function max_integer"""
        result = max_integer([0, 0, 0])
        self.assertEqual(result, 0)

    def string_(self):
        """Test for the function max_integer"""
        result = max_integer(["hola", "mundo"])
        self.assertEqual(result, mundo)

    def is_true_or_false(self):
        """Test for the function max_integer"""
        result = max_integer([False, True])
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
