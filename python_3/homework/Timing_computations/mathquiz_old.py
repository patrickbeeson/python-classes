from random import randrange
from datetime import datetime
import logging
import configparser


config = configparser.RawConfigParser()
config.read('V:/workspace/Python3_Homework13/src/mathquiz.cfg')

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


class Quiz(object):

    def generate_random(self):
        "Function to return two random integers between 1 and 10 inclusive as a list"
        random_int_one = randrange(1, 11)
        random_int_two = randrange(1, 11)
        random_int_lst = [random_int_one, random_int_two]
        logging.info('Generated random integers: {} {}'.format(random_int_one, random_int_two))
        return random_int_lst
    
    def generate_answer(self, random_int_lst):
        "Function to sum a list of integers for the question answer"
        answer = sum(random_int_lst)
        logging.info('Generated answer {} using {}.'.format(answer, random_int_lst))
        return answer
    
    def generate_question(self, random_int_one, random_int_two):
        "Function to generate a quiz question using two integers as arguments"
        question = 'What is the sum of {} and {}? '.format(random_int_one, random_int_two)
        logging.info('Generated quiz question...')
        return question
        

if __name__ == "__main__":
    # Start the timer
    quiz_start_time = datetime.now()
    # Create our quiz object
    quiz = Quiz()
    # create our question counter
    question_count = 0
    # create our time holder
    responses = {}
    # start our loop of five questions
    while question_count < 5:
        # start time
        question_start_time = datetime.now()
        # increment questions by one
        question_count += 1
        # Generate random numbers
        random_int_lst = quiz.generate_random()
        try:
            # Ask the question
            user_input = int(input(quiz.generate_question(random_int_lst[0], random_int_lst[1])))
            # Sum our random integers for our answer
            quiz_answer = quiz.generate_answer(random_int_lst)
            # Format the question
            question = 'Question #{}'.format(question_count)
            # Store the question in our dict
            responses[question] = {}
            # Log the end time
            question_end_time = datetime.now()
            # Calculate the duration
            duration = question_end_time - question_start_time
            # Add the duration for each question to our dict
            responses[question]['duration'] = duration.seconds
            # Log the answer validity to our dict for each question
            if user_input == quiz_answer:
                responses[question]['is_correct'] = 'right'
                print('{} is right!'.format(user_input))
            else:
                responses[question]['is_correct'] = 'wrong'
                print('{} is wrong!'.format(user_input))
        except ValueError:
            message = 'ValueError Exception: Input not in correct format'
            logging.error(message)
            print("Your answer wasn't an integer. Good-bye!")
            break
    # Log our quiz end time
    quiz_end_time = datetime.now()
    # Calculate our total quiz time
    duration = quiz_end_time - quiz_start_time
    # Calculate average time per question
    average = duration.seconds / question_count
    # Print our responses
    for k,v in sorted(responses.items()):
        print('{} took about {} seconds to complete and was {}'.format(k, v['duration'], v['is_correct']))
    print('You took {} seconds to finish the quiz'.format(duration.seconds))
    print('Your average time was {} seconds per question.'.format(average))
    logging.info('Quiz run successfully...')
    