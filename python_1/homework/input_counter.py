#!/usr/local/bin/python3
"""
This program accepts a string input from the user
and prints the list of words in their string with
a number representing the position of the word in the string.
"""

from string import punctuation

# Create the empty set and dict
my_set = set()
my_dict = {}

while True:
    user_input = str(input("Enter text: "))
    
    # Strip punctuation
    for punc in punctuation:
        user_input = user_input.replace(punc, "")
    
    # Stop the loop if no input is entered
    if not user_input:
        print("Finished")
        break
    
    # Create our list of words from input
    word_list = user_input.lower().split()
    
    # Assign our set size
    my_set_size = len(my_set)
    
    # Loop throught the word list, and add to the set
    for word in word_list:
        my_set.add(word)
        
        # Check if the set size has increased
        # If so, add the word and new set size to my dict
        if len(my_set) != my_set_size:
            my_set_size = len(my_set)
            my_dict[word] = my_set_size
    
    # Print the dict
    for word in (my_dict.keys()):
        print(word, my_dict[word])
