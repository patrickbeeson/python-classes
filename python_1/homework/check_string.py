#!/usr/local/bin/python3

"""
This program asks for the user to input a string.
The string is verified as being upper case with a period
at the end. If it fails, an appropriate message will be printed.
If it succeeds, a message will be printed saying it's acceptable.
"""

user_input = str(input("Enter a phrase or sentence in all upper-case, ending with a period: "))

if user_input.isupper() and user_input.endswith("."):
    print("Input meets both requirements.")
elif user_input.isupper():
    print("Input does not end with a period.")
elif user_input.endswith("."):
    print("Input is not upper-case.")
else:
    print("Input doesn't meet either requirement.")
