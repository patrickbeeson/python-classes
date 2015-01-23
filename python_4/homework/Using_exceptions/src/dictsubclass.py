"""
A subclass of the standard dict class used to
display alternative exception handling behavior.
"""

class newdict(dict):
    
    def __init__(self, default):
        super().__init__()
        self.default = default

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.default

        
        
