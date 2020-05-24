import unittest
from unittest import mock
import Example as ex

# For creating unittests simply import "unittest" and create a test class with methods for testing

class MyTest(unittest.TestCase):
    def testAddPositiv(self):
        self.assertEqual(3, ex.add(1, 2))

    def testAddNegative(self):
        self.assertEqual(-8, ex.add(-3,-5))

    def testAddWrongInput(self):
        self.assertRaises(TypeError, ex.add("a", "b"))

# Mocks can be created with the unittest library
    # Create a @mock annotation, with the function name as first example and return_value as second argument
    @mock.patch('Example.returnFalse', return_value=True)
    @mock.patch('Example.add', return_value=0)
    # Create a test function with the arguments self, and the number of mocks that are created (In this case 2)
    def mockExample(self, mock1, mock2):
        self.assertEqual(True, ex.returnFalse())
        self.assertEqual(0, ex.add(100,100))

# More information on mocks and tests: https://docs.python.org/3/library/unittest.mock.html
