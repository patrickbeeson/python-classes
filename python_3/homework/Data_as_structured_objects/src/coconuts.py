"""
API for coconut tracking
"""


class Coconut(object):
    """
    A coconut object
    """
    
    def __init__(self, coconut_type, coconut_weight):
        """
        Coconuts have type and weight attributes
        """
        self.coconut_type = coconut_type
        self.coconut_weight = coconut_weight


class Inventory(object):
    """
    An inventory object for managing Coconuts.
    """

    coconuts = []
    
    def add_coconut(self, coconut):
        """
        Add a coconut to inventory.
        Raise AttributeError if object isn't a coconut.
        """
        if isinstance(coconut, Coconut):
            self.coconuts.append(coconut)
        else:
            raise AttributeError('Only coconuts can be added to inventory.')

    def total_weight(self):
        """
        Calculate the total weight of coconuts in inventory.
        """
        weight = 0
        for coconut in self.coconuts:
            weight += coconut.coconut_weight
        return weight
