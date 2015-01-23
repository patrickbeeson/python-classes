#!/usr/local/bin/python3
"""
This program has a function that accepts three parameters. The first is required,
and the second two have default values. The function will print the value of each parameter.
The program will call the function three times: the first time with a value for the first
parameter; the second time with values for the first and second parameters; and the third
time with values for all three parameters. The program will also print the function itself.
"""

# Define our function with three parameters, one of which is required, the other two with defaults
def my_func(a, b='b was not entered', c='c was not entered'):
    print('\n'.join([a, b, c]))

# Set our test argument
test_arg = 'test'

# Pass the first (required) argument
my_func(test_arg)
# Pass the first two arguments
my_func(test_arg, test_arg)
# Pass all three arguments
my_func(test_arg, test_arg, test_arg)
# Print the function itself
print(my_func)
