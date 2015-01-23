#!/usr/local/bin/python3
""" This program accepts user input saves that input
to a file, and prints it. Upon saving, the program
will display any previous content of the file."""

# Open our input file and print the contents
prev_text = open('user_input.txt', 'r').read()
print(prev_text)

# Start the loop
while True:
    # Collect user input
    user_input = str(input('Enter text: '))
    
    # Break out of the loop if no input is captured
    if user_input == '':   
        print('Thanks for playing!')
        break
    
    # Open our input file for appending text
    inp = open('user_input.txt', 'a')
    inp.write(user_input)
    inp.close()
    
    # Open our input file to print the text
    inp_text = open('user_input.txt', 'r').read()
    print(inp_text)
