'''
Created on Nov 19, 2014

@author: pbeeson

Test the adder() function from the adder module
'''
import unittest
from adder import adder


class Test(unittest.TestCase):

    def test_adder_errors(self):
        "Tests ensuring errors in data cause validation failures."
        with self.assertRaises(TypeError):
            adder('1', 2)
        with self.assertRaises(TypeError):
            adder('1', '2')

    def test_adder_successes(self):
        "Test ensuring that valid data passes."
        self.assertEqual(adder(2, 3), (2 + 3), 'Not adding integers.')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
