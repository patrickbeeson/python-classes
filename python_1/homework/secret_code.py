#!/usr/local/bin/python3
"""
This program takes user input, and encodes it using the following cipher:
Each character of the string becomes the character whose ordinal value is 1 higher.
Then, the output of the program will be the reverse of the contructed string.
"""

# Get the user input as a string
user_input = str(input('Enter the message to be obfuscated: '))

# Create our list of letters from the string
letter_list = list(user_input)
# Create our empty changed letter list
changed_letter_list = []

# Loop through the letters in the list
for letter in letter_list:
    # Advance the ordinal number for each letter by one
    changed_letter_ord = ord(letter) + 1
    # Add our changed letters to the changed letter list
    changed_letter_list += chr(changed_letter_ord)
    
# Print a reversed changed letter list
print(''.join(reversed(changed_letter_list)))
