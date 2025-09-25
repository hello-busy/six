#!/usr/bin/env python3
"""
Tests for the six.py module
"""

import unittest
from six import is_perfect_number, factorial, get_divisors


class TestSix(unittest.TestCase):
    """Test cases for six.py functions"""
    
    def test_is_perfect_number(self):
        """Test perfect number detection"""
        self.assertTrue(is_perfect_number(6))
        self.assertTrue(is_perfect_number(28))  # Second perfect number
        self.assertFalse(is_perfect_number(12))
        self.assertFalse(is_perfect_number(1))
    
    def test_factorial(self):
        """Test factorial calculation"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(5), 120)
    
    def test_get_divisors(self):
        """Test divisor calculation"""
        self.assertEqual(get_divisors(6), [1, 2, 3, 6])
        self.assertEqual(get_divisors(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(get_divisors(1), [1])
        self.assertEqual(get_divisors(7), [1, 7])  # Prime number


if __name__ == "__main__":
    unittest.main()