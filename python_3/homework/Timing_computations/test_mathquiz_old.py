import unittest
import random
from mathquiz import *

class MathTest(unittest.TestCase):
    
    def setUp(self):
        self.quiz = Quiz()
        self.random_int_lst = self.quiz.generate_random()
    
    def test_generate_two_integers(self):
        """
        Test whether we get two integers, and they are greater than or equal to 1 or less than or equal to 10.
        """
        expected = 2
        observed = self.quiz.generate_random()
        self.assertEqual(expected, len(observed))
        self.assertIn(observed[0], range(1,11))
        self.assertIn(observed[1], range(1,11))
    
    def test_sum_of_integers(self):
        """
        Test whether we are able to sum two randomly generated integers.
        """
        rand_int_lst = self.quiz.generate_random()
        expected = sum(rand_int_lst)
        observed = self.quiz.generate_answer(rand_int_lst)
        self.assertEqual(expected, observed)

    def test_quiz_question_is_generated(self):
        """
        Test whether our quiz question is generated using two random integers.
        """
        expected = 'What is the sum of {} and {}? '.format(self.random_int_lst[0], self.random_int_lst[1])
        observed = self.quiz.generate_question(self.random_int_lst[0], self.random_int_lst[1])
        self.assertEqual(expected, observed)


if __name__ == "__main__":
    start_logging(level='info')
    unittest.main()