import unittest
from mathquiz import *
from datetime import datetime


class MathTest(unittest.TestCase):
    
    def setUp(self):
        self.question = Question()
        self.quiz = Quiz()
        self.question_start_time = datetime(2014, 12, 21, 10, 19, 28, 600000)
        self.question_end_time = datetime(2014, 12, 21, 10, 19, 28, 700000)
    
    def test_get_answer_time(self):
        """
        Test whether we get the question duration in seconds.
        """
        expected = self.question_end_time - self.question_start_time
        observed = self.question.get_answer_time(self.question_start_time, self.question_end_time)
        self.assertEqual(expected.seconds, observed)

    def test_get_question_answer(self):
        """
        Test whether we get the answer to the question.
        """
        expected = sum([self.question.num_1, self.question.num_2])
        observed = self.question.get_answer()
        self.assertEqual(expected, observed)


if __name__ == "__main__":
    start_logging(level='info')
    unittest.main()