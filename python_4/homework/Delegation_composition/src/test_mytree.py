import unittest
from mytree import Tree


class TestTree(unittest.TestCase):
    
    def setUp(self):
        self.t = Tree('B', 'Bicycle')
        
    def test_tree_walk(self):
        observed = list(self.t.walk())
        expected = ['B']
        self.assertEqual(observed, expected)
    
    def test_tree_insert(self):
        self.t.insert('P', 'Person')
        observed = list(self.t.walk())
        expected = ['B', 'P']
        self.assertEqual(expected, observed)

    def test_tree_find(self):
        observed = self.t.find('B')
        expected = 'Bicycle'
        self.assertEqual(expected, observed)
    
    def test_tree_exceptions(self):
        with self.assertRaises(KeyError):
            self.t.find('Q')
        with self.assertRaises(ValueError):
            self.t.insert('B', 'Bicycle')

if __name__ == "__main__":
    unittest.main()