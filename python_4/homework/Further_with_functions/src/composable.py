"""
composable.py: defines a composable function class.
"""
import types
class Composable:
    def __init__(self, f):
        "Store reference to proxied function."
        self.func = f
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    def __mul__(self, other):
        "Return the composition of proxied and another function."
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplication")
    def __pow__(self, exp):
        "Multiply a composable with itself exp number of times."
        if not isinstance(exp, int):
            raise TypeError('exponent must be an integer')
        if not exp > 0:
            raise ValueError('exponent must be positive')
        def anon(x):
            res = x
            for i in range(exp):
                res = self.func(res)
            return res
        return anon
        
    def __repr__(self):
        return "<Composable function {0} at 0x{1:X}>".format(
                            self.func.__name__, id(self))
