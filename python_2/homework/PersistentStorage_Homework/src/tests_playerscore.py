import unittest
import os
from playerscore import highscore
import shelve
import tempfile
import glob

class PlayerScoreTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp('testdir')
        os.chdir(self.dirname)
        self.name = 'Babe'
        self.score = 34
        self.score_higher = 35
        self.highscore_fn = os.path.join(self.dirname, 'highscore.shelve')
    
    def test_function_returns_score(self):
        with shelve.open(self.highscore_fn, writeback=True) as shelf:
            shelf[self.name] = self.score
            expected = shelf[self.name]
        self.assertEqual(expected, highscore('Patrick', 34), 'Function returns score of 34.')
    
    def test_fuction_returns_high_score(self):
        with shelve.open(self.highscore_fn, writeback=True) as shelf:
            shelf[self.name] = self.score_higher
            expected = shelf[self.name]
        first_round = highscore('Patrick', 34)
        second_round = highscore('Patrick', 35)
        self.assertEqual(expected, second_round, 'Score of 35 is greater than score of 34.')

    def tearDown(self):
        shelve_files = glob.glob(self.highscore_fn + '*')
        for fn in shelve_files:
            os.remove(fn)

if __name__ == "__main__":
    unittest.main()