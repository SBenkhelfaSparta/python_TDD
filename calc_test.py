# These are the dependencies to create and run our tests
import unittest
import pytest

from simple_calc import SimpleCalc

class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

# assertions to write our test case
# we will use basic calc example to write tests first then the code

    def test_add(self):
        # naming convention is essential to have test in the name of method
        self.assertEqual(self.calc.add(3, 2), 5) # if True test will pass
        #return num1 + num2 is being tested

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)