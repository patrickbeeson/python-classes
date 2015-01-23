#!/usr/local/bin/python3
""" Take user input, convert to float, and print
out the number to two decimal places, with commas. """

import funcs

while True:
    inval = input("Enter a number: ")
    if not inval:
        break
    number = float(inval)
    print(funcs.commareal("{0:.2f}".format(number)))
