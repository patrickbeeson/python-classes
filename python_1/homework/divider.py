#!/usr/local/bin/python3
"""
This program uses a while loop to request an integer
from the user, and binds it to a variable. Then, it 
divides the value of 10 by the stored integer and 
prints the results. A try statement, followed by a series
of exceptions is used to catch ValueError and ZeroDivisionError.
When caught, the responses are printed to the user.
"""

# start the loop
while True:
    # get our input
    user_input = input('Provide an integer: ')
    # if the input is blank, quit
    if not user_input:
        print("Goodbye")
        break
    # begin catching exceptions
    # if kosher, print the result of our division
    try:
        print(10/int(user_input))
    except ValueError:
        print("Your input must be an integer!")
    except ZeroDivisionError:
        print("Your input must not be zero (0)")
