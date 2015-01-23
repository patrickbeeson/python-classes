"""
Coconuts test program 
"""
import unittest
from coconuts import Coconut, Inventory

class TestCoconuts(unittest.TestCase):
    
    def setUp(self):
        # Create our coconuts
        self.south_asian = Coconut(coconut_type="South Asian", coconut_weight=3)
        self.middle_eastern = Coconut(coconut_type="Middle Eastern", coconut_weight=2.5)
        self.american = Coconut(coconut_type="American", coconut_weight=3.5)
        self.inventory = Inventory()
        # Peanut object for testing instance
        class Peanut(object):
            pass
        self.peanut = Peanut()
    
    def test_coconut_varities(self):
        """
        Test different coconut types have different weights
        """
        self.assertNotEqual(self.middle_eastern.coconut_weight, self.south_asian.coconut_weight)

    def test_coconut(self):
        """
        Test add_coconut method accepts only coconut types as argument.
        """
        with self.assertRaises(AttributeError):
            self.inventory.add_coconut(self.peanut)

    def test_coconut_weight(self):
        """
        Test total_weight method calculates total weight of coconuts in inventory.
        """
        # Two South Asians
        self.inventory.add_coconut(self.south_asian)
        self.inventory.add_coconut(self.south_asian)
        # Three Americans
        self.inventory.add_coconut(self.american)
        self.inventory.add_coconut(self.american)
        self.inventory.add_coconut(self.american)
        # One Middle Eastern
        self.inventory.add_coconut(self.middle_eastern)
        expected = (self.south_asian.coconut_weight * 2) + (self.american.coconut_weight * 3) + self.middle_eastern.coconut_weight
        observed = self.inventory.total_weight()
        self.assertEqual(expected, observed)

if __name__ == "__main__":
    unittest.main()
