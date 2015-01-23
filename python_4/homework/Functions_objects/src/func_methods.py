"""
func_methods.py: A subclass of str type with methods "<<" and ">>" to perform
cyclic shifting of characters in a string.
"""


class sstr(str):
    """
    An sstr object subclassing str object.
    """
    def __init__(self, string):
        "Delegate method calls to parent while adding string attribute"
        self.string = string
        super().__init__()

    def __lshift__(self, shift):
        "Shift characters to the left."
        return sstr('{}'.format(self.string[shift:] + self.string[:shift]))
    
    def __rshift__(self, shift):
        "Shift characters to the right."
        return sstr('{}'.format(self.string[-shift:] + self.string[:-shift]))

