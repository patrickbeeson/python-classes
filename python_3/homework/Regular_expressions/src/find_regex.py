"""
find_regex.py
"""
import re

def phrasematch(phrase, text_to_search):
    """
    Function that takes two arguments: the first for a phrase
    to match, the second for the text to search. Start and end
    indices are returned.
    """
    m = re.search(phrase, text_to_search)
    return (m.start(), m.end())
