#!/usr/local/bin/python3
""" A program designed to display switching in Python """

import sys
import courses

def print_text(text, *args, **kwargs):
    """ Print just the text value """
    print('text: ' + text)

def print_args(text, *args, **kwargs):
    """ Print just the argument list """
    print('args:')
    for i, arg in enumerate(args):
        print('{0}: {1}'.format(i, arg))

def print_kwargs(text, *args, **kwargs):
    """ Print just the keyword arguments """
    print('keyword args: ')
    for k, v in kwargs.items():
        print('{0}: {1}'.format(k, v))

def print_all(text, *args, **kwargs):
    print_text(text, *args, **kwargs)
    print_args(text, *args, **kwargs)
    print_kwargs(text, *args, **kwargs)

def quit(text, *args, **kwargs):
    """ Terminates the program """
    print("Quitting the program")
    sys.exit()

if __name__ == '__main__':
    switch = {
        'text': print_text,
        'args': print_args,
        'kwargs': print_kwargs,
        'all': print_all,
        'courses': courses.description,
        'quit': quit
    }
    
    options = switch.keys()
    prompt = 'Pick an option from the list ({0}): '.format(', '.join(options))
    while True:
        inp = input(prompt)
        option = switch.get(inp, None)
        if option:
            option('Python', 'is', 'fun', course="Python 101", publisher="O'Reilly")
            print('- ' * 40)
        else:
            print('Please select a valid option!')

    