#!/usr/local/bin/python3
"""This program asks a user to guess a number.
Each guess will be checked against a secret number stored
in a variable (between 1 and 20). It will tell the user
whether their guess was higher or lower than the secret.
If the user guesses correctly, the program will terminate.
It will also keep track of the number of guesses, and terminate 
after five incorrect guesses. The program will print a message if
the user guessed the number correctly."""

import random

# Assign the secret number at random between 1 and 20
secret = random.randrange(1, 21)
# Set guess count to 0
guess_count = 0

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
        print("You guessed correctly! The secret was {}.".format(secret))
        break
    elif user_input > secret:
        print("Your guess was too high. Try a lower number.")
    elif user_input < secret:
        print("Your guess was too low. Try a higher number.")
    
    # Increment the guess count by 1
    guess_count += 1
    
    if guess_count == 5:
        print("You ran out of guesses! The secret was {}".format(secret))
        break