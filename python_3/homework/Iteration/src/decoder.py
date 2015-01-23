"""
decoder.py: Program to convert integers between 1 and 26 to a corresponding letter.
"""

def alphabator(lst):
    """
    Returns generator that converts int objects between 1 and 26
    into the corresponding letter while also returning ints outside
    that range.
    """
    n = 0
    for item in lst:
        n += 1
        if isinstance(item, int) and 1 <= item <= 26:
            item = chr(64 + item)
        yield item
