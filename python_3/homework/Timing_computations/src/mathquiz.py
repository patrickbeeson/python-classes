from random import randrange
from datetime import datetime, timedelta
import logging
import configparser


config = configparser.RawConfigParser()
config.read('mathquiz.cfg')

LOG_FILENAME = config.get('log', 'output')
LOG_FORMAT = config.get('log', 'format')
DEFAULT_LOG_LEVEL = config.get('log', 'default_level')
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }


def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    logging.info('Starting up the quiz program')


class Question(object):
    logging.info('Created question object')

    def __init__(self):
        self.num_1 = randrange(1, 11)
        self.num_2 = randrange(1, 11)

    def get_answer_time(self, start_time, end_time):
        delta = end_time - start_time
        logging.info('Returned question answer time of {}'.format(delta.seconds))
        return delta.seconds

    def get_answer(self):
        answer = sum([self.num_1, self.num_2])
        logging.info('Returned question answer of {}'.format(answer))
        return answer

    def __str__(self):
        return 'What is the sum of {} and {}? '.format(self.num_1, self.num_2)


class Quiz(object):
    logging.info('Created quiz object')

    def __init__(self):
        self.question_count = 5
        self.question_lst = [Question() for i in range(self.question_count)]
        self.answer_data = {}

    def run_quiz(self):
        for index, question in enumerate(self.question_lst, start=1):
            start_time = datetime.now()
            try:
                user_input = int(input(question.__str__()))
            except ValueError:
                print('Bad input')
                break
            end_time = datetime.now()
            question_index = 'Question #{}'.format(index)
            self.answer_data[question_index] = {}
            self.answer_data[question_index]['duration'] = question.get_answer_time(start_time, end_time)
            if user_input == question.get_answer():
                self.answer_data[question_index]['validity'] = 'right'
                print('{} is right!'.format(user_input))
            else:
                self.answer_data[question_index]['validity'] = 'wrong'
                print('{} is wrong!'.format(user_input))
        logging.info('Ran quiz')

    def print_results(self):
        question_duration_lst = []
        for k, v in sorted(self.answer_data.items()):
            print('{} took about {} seconds and was {}'.format(k, v['duration'], v['validity']))
            question_duration_lst.append(v['duration'])
        print('You took {} seconds to finish the quiz.'.format(sum(question_duration_lst)))
        print('Your average time was {} seconds per question.'.format(sum(question_duration_lst) / self.question_count))
        logging.info('Printed quiz results.')


if __name__ == "__main__":
    start_logging(level='info')
    quiz = Quiz()
    quiz.run_quiz()
    quiz.print_results()