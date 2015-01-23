"""
Demonstrate the difference between match() and search().
"""
import re

def check_number(text):
    regex = r"(\d\d\d|\(\d\d\d))(-| )\d\d\d-\d\d\d\d"
    match = re.match(regex, text)
    if match:
        return match.group()
    match = re.search(regex, text)
    if match:
        return len(text)
