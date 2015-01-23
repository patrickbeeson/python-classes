#!/usr/local/bin/python3

from sys import argv
from string import punctuation
from collections import Counter as counter
from operator import itemgetter

def strip_punc(text):
    """ This function strips punctuation from a
    string passed as an argument.
    """
    # Keep '&' since it counts as a word    
    # Loop through text and remove punctuation
    for punc in punctuation.replace("&", ""):
        text = text.replace(punc, "")
    
    return text


def compute_text(filename):
    """ This function reads input from a file, 
    splits the words into a list, and computes
    the length of each word. It then prints a
    table showing the word count for each
    of the word lengths.
    """
    # Open our file
    try:
        with open(filename, 'r') as f:
            # Read the file
            data = f.read()
        
            # Strip the punctuation
            data = strip_punc(data)

            # Print the headers
            print('{:>7}{:>10}'.format('Length', 'Count'))
        
            # Use counter to get a dictionary of our lengths and values from data
            length_count_lst = counter([len(word) for word in data.lower().split()])
        
            # Create a sorted list (by length) of tuples
            sorted_lst = sorted(length_count_lst.items(), key=itemgetter(0))
        
            # Print our items
            for item in sorted_lst:
                print('{!s:>8}{!s:>10}'.format(item[0], item[1]))
    except FileNotFoundError:
        print("Your file cannot be found.")
    except TypeError:
        print("You didn't enter a file.")
    except:
        print("Unknown error.")


if __name__ == "__main__":

    try:
        filename_input = argv[1]
        compute_text(filename_input)
    except IndexError:
        print("You didn't enter a filename.")