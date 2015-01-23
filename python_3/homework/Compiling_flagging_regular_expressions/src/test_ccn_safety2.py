import unittest
from ccn_safety2 import mask_cc

class TestCcnSafety(unittest.TestCase):
    
    def setUp(self):
        self.text = 'Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts.'
        self.returned_text =  "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts."
        
    def test_mask_cc(self):
        result, count = mask_cc(self.text)
        self.assertFalse("5555-5555-5555-5555" in result)
        self.assertTrue("555-123-4567" in result)
        self.assertTrue("CCN REMOVED FOR YOUR SAFETY" in result)
        self.assertEqual(result, self.returned_text)
        self.assertEqual(2, count)

if __name__ == "__main__":
    unittest.main()
