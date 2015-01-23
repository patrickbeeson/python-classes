"""
ccn_safety.py
"""
import re

def mask_cc(text):
    """
    Function to mask all but the last four digits of a credit card number
    from a text argument.
    """
    return re.subn(r"\d{4}-\d{4}-\d{4}", "XXXX-XXXX-XXXX", text)