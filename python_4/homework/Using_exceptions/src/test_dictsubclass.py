import unittest
from dictsubclass import newdict

class TestDictSub(unittest.TestCase):
    
    def setUp(self):
        self.ndict = newdict(default='test')

    def test_default_is_returned_on_keyerror_exception(self):
        expected = 'test'
        observed = self.ndict['testing']
        self.assertEqual(expected, observed)

if __name__ == "__main__":
    unittest.main()