"""
furnishings.py
"""

class Furnishing(object):
    """
    The parent Furnishing class for furniture objects.
        Room is the room in which the furniture exists.
        Type is the type of furniture being called.
        Count is the number of objects that exist for the object type.
    """
    count = 0
    
    def __init__(self, room):
        self.room = room
        self.type = self.__class__.__name__
        self.__class__.count += 1


class Sofa(Furnishing):
    " A sofa object "
    pass


class Bookshelf(Furnishing):
    " A bookshelf object "
    pass


class Bed(Furnishing):
    " A bed object "
    pass


class Table(Furnishing):
    " A table object "
    pass

def map_the_home(furniture_list):
    """
    Function to create a dict mapping rooms to furnishings objects.
    Accepts a list of furnishings objects as an argument.
    """
    d = dict()
    for furniture in furniture_list:
        room = furniture.room
        if room not in d:
            d[room] = []
        d[room].append(furniture)
    return d

def counter(furniture_list):
    """
    Function to print the types of furniture and how many of each type.
    Accepts a list of furnishing objects as an argument.
    """
    d = dict()
    for furniture in furniture_list:
        d[furniture.type] = furniture.count
    return '\n'.join('{}s: {}'.format(key, value) for key, value in sorted(d.items()))
