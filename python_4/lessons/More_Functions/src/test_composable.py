"""
test_composable.py: performs simple tests of composable functions
"""
import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing"
    return s[::-1]

def square(x):
    "Multiplies a number by itself"
    return x*x

class ComposableTestCase(unittest.TestCase):
    
    def test_inverse(self):
        reverser = Composable(reverse)
        nulltran = reverser * reverser
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEquals(nulltran(s), s)
    
    def test_square(self):
        squarer = Composable(square)
        po4 = squarer * squarer
        for v, r in ((1, 1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)
    
    def test_exceptions(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc

if __name__ == "__main__":
    unittest.main()