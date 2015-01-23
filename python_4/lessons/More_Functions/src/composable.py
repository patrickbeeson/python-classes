"""
composable.py: defines a composable function class.
"""
import types

class Composable:
    def __init__(self, f):
        "Store reference to the proxied function"
        self.func = f
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through"
        return self.func(*args, **kwargs)
    def __mul__(self, other):
        "Returns the composition of the proxied and another function"
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError('Illegal operands for multiplication')
    def __repr__(self):
        return "<Composable function {0} at 0x{1:X}>".format(self.func.__name__, id(self))
