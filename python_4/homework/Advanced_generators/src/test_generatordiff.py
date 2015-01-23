import unittest
from generatordiff import rand_gen
from random import sample


class TestGeneratorDiff(unittest.TestCase):
    
    def setUp(self):
        self.rand_lst = sample(range(1, 1000001), 1000000)

    def test_list_of_a_million_random_numers(self):
        "Ensure we are getting the list of numbers as expected"
        observed = self.rand_lst
        self.assertEqual(len(observed), 1000000)
        self.assertEqual(min(observed), 1)
        self.assertEqual(max(observed), 1000000)
    
    def test_generator_of_a_million_random_numers(self):
        "Ensure our generator returns the list of numbers as expected"
        observed = [x for x in rand_gen()]
        expected = 1000000
        self.assertEqual(len(observed), 1000000)
        self.assertEqual(min(observed), 1)
        self.assertEqual(max(observed), 1000000)

if __name__ == "__main__":
    unittest.main()
