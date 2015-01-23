"""
context_mgr.py: Program to suppress any ValueError exception that occur in
the context of a suite controlled by a context manager. Other exceptions are allowed
to be raised.
"""


class Context(object):
    """
    Context manager class object.
    """
    
    def __init__(self, raising=True):
        self.raising = raising
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        # if a ValueError is found, suppress it accordingly
        if not exc_type == ValueError:
            return not self.raising
        else:
            return self.raising
        
if __name__ == "__main__":
    with Context():
        raise ValueError('error suppressed')
    
    with Context()as c:
        raise TypeError('error not suppressed')
