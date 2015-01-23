import unittest
from classFactory import build_row
import mysql.connector
from database import login_info

class DBTest(unittest.TestCase):
    
    def setUp(self):
        C = build_row("user", "id name email")
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])
        Animal_Row = build_row("animal", "id name family weight")
        self.actual_animal = Animal_Row([1, "Ellie", "Elephant", 2350])
    
    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")
    
    def test_repr(self):
        self.assertEqual(repr(self.c),
                         "user_record(1, 'Steve Holden', 'steve@holdenweb.com')")
    
    def test_retrieve(self):
        db = mysql.connector.Connect(**login_info)
        curs = db.cursor()
        condition = 'weight > 2000'
        for data_row in self.actual_animal.retrieve(curs, condition):
            animal = data_row
        self.assertEqual(repr(animal), "animal_record(1, 'Ellie', 'Elephant', 2350)")

    def test_retrieve_no_condition(self):
        db = mysql.connector.Connect(**login_info)
        curs = db.cursor()
        for data_row in self.actual_animal.retrieve(curs):
            animal = data_row
        self.assertEqual(repr(animal), "animal_record(7, 'Zorro', 'Zebra', 340)")


if __name__ == "__main__":
    unittest.main(warnings='ignore')
