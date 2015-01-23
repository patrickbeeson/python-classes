"""
String regular expressions
"""

import re

def city_search(text):
    
    regex = r"[A-Z][a-z]+(\s[A-Z][a-z]+)*,\s[A-Z]{2}\s\d{5}"
    
    search = re.search(regex, text)
    if search:
        return search.group()
