#!/usr/local/bin/python3

from string import punctuation

def strip_punc(text):
    """ This function strips punctuation from a
    string passed as an argument.
    
    >>> strip_punc('Check it out! Any punctuation here?')
    'Check it out Any punctuation here'
    """
    for punc in punctuation:
        text = text.replace(punc, "")
    
    return text


def compute_text(filename):
    """ This function reads input from a file, 
    splits the words into a list, and computes
    the length of each word. It then prints a
    table showing the word count for each
    of the word lengths.

    >>> compute_text('filename_test.txt')
    Length Count
    1 4
    2 2
    3 1
    4 4
    5 4
    6 9
    7 11
    8 4
    9 2
    """
    with open(filename, 'r') as f:
        data = f.read()
        
        data = strip_punc(data)
    
        word_list = data.split()
        
        print('Length Count')
        
        for i, word in enumerate(word_list, 1):
            print('{} {}'.format(i, len(word)))

def _test():
    import doctest, final
    return doctest.testmod(final)

if __name__ == "__main__":
    _test()