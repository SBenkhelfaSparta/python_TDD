# TDD - Test Driven Development

- Let's dive into coding
- We have already completed step 1 and 2 (Repo and Pycharm project)
- Step 3 is creating a file called calc_test.py
- We will use `unittest` and `pytest`
- `pip install pytest`
- `python -m unittest`
- `python -m unittest discover -v`

## How tests work
- Import the class you are testing
- Create an object of that class
- Name your method in the test file "test_" followed by the name of the method you are going to create/test
- Syntax for the test logic is `self.assertEqual(self.class_object.method_name(x, y), z)` where `x` and `y` are the inputs and `z` is the expected output

Here is an example of test code:

```python
class SimpleCalc:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2
```
Above is the functional class and below is the test class.
```python
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
```