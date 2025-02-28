# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.


# def subtract_divide(dividend, x, y):
#     try:
#         z = x - y
#         return dividend / z
#     except ZeroDivisionError:
#         raise CustomZeroDivsionError(f"This won't work because {x} - {y} = 0.")

import unittest
import mymath

class TestMyMath(unittest.TestCase):
    def test_subtract_divide(self):
        self.assertEqual(mymath.subtract_divide(16, 64, 32), 0.5)

    def test_subtract_divide_raises_exception(self):
        with self.assertRaises(mymath.CustomZeroDivsionError):
            mymath.subtract_divide(20, 7, 7)

if __name__ == 'main':
    unittest.main()
