#!/usr/local/bin/python3
"""
guessing_game.py
This program imports the random module to generate a random number
between 1 and 99 stored as a variable. It then accepts integers from the user
to compare against the saved random number. If the guess is successful, it informs
the user and terminates. Otherwise, it tells the user whether the guess should be
higher or lower and allows them to guess again.
"""

import random

# Assign the secret number at random between 1 and 99
secret = random.randrange(1, 100)

while True:
    # Grab user input as string to check if it's blank
    user_input = str(input("Guess a number: "))
    
    if not user_input:
        print("You didn't enter a guess!")
        continue
    elif not user_input.isdigit():
        print("Each guess should be a number.")
        continue
    else:
        # Convert to an integer for comparison
        user_input = int(user_input)
    
    if user_input == secret:
        print("You guessed correctly!")
        break
    elif user_input > secret:
        print("Your guess was too high.")
    elif user_input < secret:
        print("Your guess was too low.")
