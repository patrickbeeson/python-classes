#!/usr/local/bin/python3

# our list of small words
small_words = ['into', 'the', 'a', 'of', 'at', 'in', 'for', 'on']

def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    # break our title into a list of lowercase words
    lst_of_words = title.lower().split()
    # if there are no words in the list, return nothing
    if not lst_of_words:
        return ''
    # Our default title is the first word in the list, capitalized
    new_title = [lst_of_words[0].capitalize()]
    # Loop through the words in the list
    for word in lst_of_words[1:]:
        # Append to the new_title object any small words or the capitalized words
        new_title.append(word in small_words and word or word.capitalize())
    # Format our returned new_title
    return " ".join(new_title)

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()