"""
Demonstrate string representations using inheritance
"""


class Person(object):
    "A person object"
    def __init__(self, name):
        self.name = name


class NamedPerson(Person):
    "Represents a person using their name"
    def __str__(self):
        return self.name
