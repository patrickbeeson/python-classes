import unittest
from func_methods import sstr


class TestFuncMethods(unittest.TestCase):
    
    def setUp(self):
        self.s1 = sstr("abcde")

    def test_object_returns_string(self):
        expected = "abcde"
        self.assertEqual(expected, self.s1)

    def test_returns_lshift_two(self):
        expected = 'cdeab'
        observed = self.s1 << 2
        self.assertEqual(expected, observed)

    def test_returns_lshift_zero(self):
        expected = 'abcde'
        observed = self.s1 << 0
        self.assertEqual(expected, observed)

    def test_returns_rshift_two(self):
        expected = 'deabc'
        observed = self.s1 >> 2
        self.assertEqual(expected, observed)

    def test_returns_rshift_zero(self):
        expected = 'abcde'
        observed = self.s1 >> 0
        self.assertEqual(expected, observed)

    def test_returns_rshift_five(self):
        expected = 'abcde'
        observed = self.s1 >> 5
        self.assertEqual(expected, observed)

    def test_multi_shifts(self):
        expected = True
        observed = (self.s1 >> 5) << 5 == 'abcde'
        self.assertEqual(expected, observed)

if __name__ == "__main__":
    unittest.main()