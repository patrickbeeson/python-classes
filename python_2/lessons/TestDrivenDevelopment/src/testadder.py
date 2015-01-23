"""
Demonstrates the fundementals of unittest.
add() is a function that lets you 'add' integers, strings and lists.
"""

from adder import adder

import unittest
class TestAdder(unittest.TestCase):
    
    def test_numbers(self):
        self.assertEqual(adder(3, 4), 7, '3 + 4 should be 7')
    
    def test_strings(self):
        self.assertEqual(adder('x', 'y'), 'xy', 'x + y should be xy')
    
    def test_lists(self):
        self.assertEqual(adder([1,2],[3,4]), [1,2,3,4], "[1,2] + [3,4] should be [1,2,3,4]")
    
    def test_number_and_string(self):
        self.assertEqual(adder(1,'two'), '1two', '1 + two should be 1two')
    
    def test_numbers_and_list(self):
        self.assertEqual(adder(4,[1,2,3]), [1,2,3,4], "4 + [1,2,3] should be [1,2,3,4]")

if __name__ == "__main__":
    unittest.main()
