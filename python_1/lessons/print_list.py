#!/usr/local/bin/python3

def print_list(lst, rev=False):
     """ Prints the contents of a list. """
     if rev:
         lst = reversed(lst)
     for i in lst:
         print(i)

print_list(['Printing', 'a', 'list'])
print()
print_list(['Printing', 'a', 'reversed', 'list'], True)
print()
print_list(lst=['A', 'list', 'with', 'specified', 'arguments'], rev=False)
