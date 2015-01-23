import unittest
from phone import get_phone, text


class TestRegex(unittest.TestCase):
    
    def test_phone(self):
        numbers = get_phone(text)
        self.assertEqual(len(numbers), 5)


if __name__ == "__main__":
    unittest.main()
