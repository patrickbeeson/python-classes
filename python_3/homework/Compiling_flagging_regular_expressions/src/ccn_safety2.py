"""
ccn_safety2.py
"""
import re

def mask_cc(text):
    """
    Function to mask a credit card number
    from a text argument with 'CCN REMOVED FOR YOUR SAFETY'.
    """
    regex = re.compile(r"""\d{4} # first four digits
        -\d{4} # second four digits
        -\d{4} # third four digits
        -\d{4} # fourth four digits
    """, re.VERBOSE)
    return regex.subn("CCN REMOVED FOR YOUR SAFETY", text)