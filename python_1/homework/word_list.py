#!/usr/local/bin/python3
"""
This program reads a string from a user to create
a list of words from the input. It then creates two
lists, one containing words that contain at least one
upper-case letter, and one of the words without upper-
case letters. It then prints out the words with upper-
case letters, followed by those without, with one word
per line.
"""
from re import findall
from string import ascii_uppercase

user_input = str(input("Input your text: "))

# Create our list of words from input
word_list = user_input.strip().split()

# Create our empty lists
upper_case_words = []
lower_case_words = []

# Loop through each word in the list
for word in word_list:
    # Use regex to find uppercase characters in each word
    # Append the word to the appropriate list
    if findall('[A-Z]', word):
        upper_case_words.append(word)
    else:
        lower_case_words.append(word)

# Print the upper case list first, followed by the lower case list.
print("\n".join(upper_case_words + lower_case_words))
