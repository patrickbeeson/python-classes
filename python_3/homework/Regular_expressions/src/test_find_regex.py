import unittest
from find_regex import phrasematch


class TestFindRegex(unittest.TestCase):
    
    def setUp(self):
        self.text = 'In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called "regular sets" as a method to do pattern matching. Active usage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer.'

    def test_function_accepts_phrase_and_returns_indices(self):
        "Tests whether the function returns the expected indices."
        expected = (231, 250)
        observed = phrasematch('Regular Expressions', self.text)
        self.assertEqual(expected, observed)


if __name__ == "__main__":
    unittest.main()
