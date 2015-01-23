#!/usr/local/bin/python3
"""
This program uses a while loop to request an integer
from the user, and binds it to a variable. Then, it 
divides the value of 10 by the stored integer and 
prints the results. A try statement, followed by a series
of exceptions is used to catch ValueError and ZeroDivisionError.
When caught, the responses are printed to the user.
"""

def divider(value):
    """ Return the result of dividing the value by 10 """
    try:
        return 10/int(value)
    except ValueError:
        print("Your input must be an integer!")
    except ZeroDivisionError:
        print("Your input must not be zero (0)")


if __name__ == "__main__":    

    while True:
        user_input = input('Provide an integer: ')
        if not user_input:
            print("Goodbye")
            break
        print(divider(user_input))