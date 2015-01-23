#!/usr/local/bin/python3
""" Demonstrates capture of keyword arguments """

def keywords(**kwargs):
    "Prints the keys and arugments passed through"
    for key in kwargs:
        print("{0}: {1} ".format(key, kwargs[key]))
    
def keywords_as_dict(**kwargs):
    "Returns the keyword arguments as a dict"
    return kwargs

if __name__ == "__main__":
    keywords(guido="Founder of Python", python="Used by NASA and Google")
    print(keywords_as_dict(guido="Founder of Python", python="Used by NASA and Google"))
