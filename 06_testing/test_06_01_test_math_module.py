# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import unittest
import math

class TestMathModule(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(math.sqrt(16), 4)

    def test_factorial(self):
        self.assertEqual(math.factorial(3), 6)

if __name__ == 'main':
    unittest.main()