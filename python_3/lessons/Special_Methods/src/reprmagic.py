"""
Demonstrate differences between __str__() and __repr__()
"""


class neither(object):
    pass


class stronly(object):
    def __str__(self):
        return "STR"


class repronly(object):
    def __repr__(self):
        return "REPR"


class both(stronly, repronly):
    pass


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name
    def __repr__(self):
        return "Person ({0.name!r}, {0.age!r})".format(self)
