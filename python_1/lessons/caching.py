#!/usr/local/bin/python3
""" Demonstrates caching """

global_cache = {}

def kid(a, b):
    """ Multiplication the hard way """
    if (a,b) in global_cache:
        return global_cache[(a,b)]

    c = 0
    for i in range(b):
        c += a
    global_cache[(a,b)] = c
    return c
    
while True:
    a = input('enter a number: ')
    b = input('enter another number: ')
    a = int(a)
    b = int(b)
    print(kid(a,b))
    print(global_cache)
    print('-'*40)

