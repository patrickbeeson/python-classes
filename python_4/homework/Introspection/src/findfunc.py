"""
Program to take module as argument, 
and print all functions and their arguments as they would appear in a def statement.
"""
from inspect import getmembers, isfunction, getfullargspec, formatargspec
from importlib import import_module


class FuncFinder(object):
    """
    A FuncFinder object
        module    The module being imported for introspection
        func_lst    The list of functions from the module imported
    """
    def __init__(self, module):
        self.module = import_module(module)
        self.func_lst = getmembers(self.module, isfunction)

    def get_funclst_argspec(self):
        "Returns formatted arg spec for functions as generator"
        func_specs = ('def {}{}'.format(func[0], formatargspec(*getfullargspec(func[1]))) for func in self.func_lst)
        return func_specs

if __name__ == "__main__":
    """
    Demonstrate how calling the get_funclst_argspec method on our
    class creates a generator capable of printing expected output.
    """
    funcfinder = FuncFinder('json')
    for func in funcfinder.get_funclst_argspec():
        print(func)
