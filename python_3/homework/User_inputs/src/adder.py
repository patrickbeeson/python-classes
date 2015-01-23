"""
adder.py: Function to accept two arguments, and add them together.
Only works if the arguments are integers. Otherwise, raises TypeError.
"""

def adder(obj_1, obj_2):
    """Validates arguments as integer and add together."""
    if isinstance(obj_1, int) and isinstance(obj_2, int):
        return obj_1 + obj_2
    else:
        raise TypeError('Not an integer')
