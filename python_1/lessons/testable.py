#!/usr/local/bin/python3
""" Demonstrates the doctest module in action """

def square(x):
    ''' Returns the square of a numeric argument.
    
    >>> square(3)
    9
    >>> square(1000)
    1000000
    >>> square("x")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
    '''
    return x**2
    
def _test():
    import doctest, testable
    return doctest.testmod(testable)
    
if __name__ == "__main__":
    _test()