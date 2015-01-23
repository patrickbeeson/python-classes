"""
centipede.py
"""


class Centipede(object):
    """
    A centipede object
    """

    def __init__(self):
        "Function to initialize empty lists for stomach and legs."
        self.__dict__['stomach'] = []
        self.__dict__['legs'] = []

    def __call__(self, *args):
        "Function to store data passed to instance in stomach list."
        for arg in args:
            self.stomach.append(arg)

    def __setattr__(self, key, value):
        "Function to set attributes for instance while preventing overrides of stomach or legs."
        if key == 'stomach' or key == 'legs':
            raise AttributeError('{0} is for internal use only'.format(key))
        self.__dict__[key] = value
        self.legs.append(key)

    def __repr__(self):
        "Function to return a list of attributes for the instance (legs)."
        return ','.join(self.legs)

    def __str__(self):
        "Function to return the contents of the stomach."
        return ','.join(self.stomach)
