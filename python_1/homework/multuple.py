#!/usr/local/bin/python3
"""
This program takes data (integers) and prints the results of multiplying
the two numbers together. String formatting ensures it's displayed nicely.
"""
# Create our two-element tuples
initial_data = (
    (1, 1),
    (2, 2),
    (12, 13),
    (4, 4),
    (99, 98)
)

# Loop through the tuples
for (a, b) in initial_data:
    # Multiply the two numbers
    result = a * b
    # Format the results
    fmt = "{result:>4} = {a:>2} x {b:>2}"
    # Print the formatted results
    print(fmt.format(result=result, a=a, b=b))
