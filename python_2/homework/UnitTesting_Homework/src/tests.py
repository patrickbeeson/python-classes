""" Tests the title function using unittest. """
import unittest

def title(s):
    """
    How close is this function to str.title()?
    """
    return s[0].upper()+s[1:]

def fixed_title(s):
    """
    How close is this function to str.title()?
    Note: The original function has been updated to match
    the native method.
    """
    return s[0].upper()+s[1:].lower()

class TestTitle(unittest.TestCase):
    
    def test_uppercasing_of_first_letter(self):
        test = 'test'
        self.assertTrue(title(test), 'Test')
        self.assertEqual(title(test), test.title(), "'Test' matches 'Test'")
        self.assertEqual(fixed_title(test), test.title(), "'Test' matches 'Test'")
    
    def test_first_letter_already_uppercase(self):
        test = 'TEST'
        self.assertTrue(title(test), 'Test')
        self.assertNotEqual(title(test), test.title(), "'TEST' doesn't match 'Test'")
        self.assertEqual(fixed_title(test), test.title(), "'Test' matches 'Test'")
        
    def test_bad_input(self):
        test = 2
        self.assertRaises(TypeError, title)
        
    def test_missing_input(self):
        test = ''
        self.assertRaises(TypeError, title)
        
if __name__ == '__main__':
    unittest.main()