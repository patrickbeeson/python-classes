#!/usr/local/bin/python3
"""
caser.py
This program has the following functions:

capitalize: accepts a string and applies the capitalize method
title: accepts a string and applies the title method
upper: accepts a string and applies the upper method
lower: accepts a string and applies the lower method
exit: ends the program

These functions are stored in a dict with keys maching function names.
A while loop requests two inputs from the user: the function and a string. Function
dispatch is used to get the correct function based on the first input, with the string applied as
the second input.
"""

import sys

def capitalize(text):
    """ Applies the capitalize method to a string. """
    print(text.capitalize())
    
def title(text):
    """ Applies the title method to a string. """
    print(text.title())
    
def upper(text):
    """ Applies the upper method to a string. """
    print(text.upper())

def lower(text):
    """ Applies the lower method to a string. """
    print(text.lower())

def exit(text):
    """ Ends the program """
    print('Thanks for using this program!')
    return sys.exit()

if __name__ == "__main__":
    # Create our function dispatch table
    switch = {
        'capitalize': capitalize,
        'title': title,
        'upper': upper,
        'lower': lower,
        'exit': exit
    }
    
    # Get the keys from our table
    options = switch.keys()
    # Create the function options for our user input
    prompt = 'Enter a function name ({0}): '.format(', '.join(options))
    
    while True:
        # Get the user's function choice
        function_choice = str(input(prompt))
        # If the function exists, assign it to option object
        # If not, assign to None
        option = switch.get(function_choice, None)
        if option:
            # Get the string argument
            option(input('Enter a string: '))
        else:
            # Ensure the user specifies a valid function
            print('Please select a valid option!')
