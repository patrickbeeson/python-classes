import unittest
from furnishings import *


class TestFurnishing(unittest.TestCase):
    
    def setUp(self):
        self.home = []
        self.sofa_1 = Sofa('Living room')
        self.sofa_2 = Sofa('Entertainment nook')
        self.bed_1 = Bed('Master bedroom')
        self.bed_2 = Bed('Guest bedroom')
        self.home.append(self.sofa_1)
        self.home.append(self.sofa_2)
        self.home.append(self.bed_1)
        self.home.append(self.bed_2)

    def test_map_at_home_function(self):
        " Test map_at_home function returns dict as expected"
        expected = {self.sofa_1.room: [self.sofa_1], self.sofa_2.room: [self.sofa_2], self.bed_1.room: [self.bed_1], self.bed_2.room: [self.bed_2]}
        observed = map_the_home(self.home)
        self.assertEqual(expected, observed)

    def test_counter_function(self):
        " Test counter function returns objects and count as expected"
        expected = "Beds: 2" + "\n" + "Sofas: 2"
        observed = counter(self.home)
        self.assertEqual(expected, observed)

if __name__ == "__main__":
    unittest.main()
