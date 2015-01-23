#!/usr/local/bin/python3

def structure_list(text):
    """ Returns a list of punctuation in a text and the location of the word 'Python' in a text"""
    
    punctuation_marks = "!?.,:;"
    punctuation = []
    for mark in punctuation_marks:
        if mark in text:
            punctuation.append(mark)
        return punctuation, text.find('Python')

text_block = """\
Python is used everywhere nowadays.
Major users include Google, Yahoo!, CERN and NASA (a team of 40 scientists and engineers
is using Python to test the systems supporting the Mars Space Lander project).
ITA, the company that produces the route search engine used by Orbitz, CheapTickets,
travel agents and many international and national airlines, uses Python extensively.
The YouTube video presentation system uses Python almost exclusively, despite their
application requiring high network bandwidth and responsiveness.
This snippet of text taken from chapter 1"""

for line in text_block.splitlines():
    print(line)
    p, l = structure_list(line)
    if p:
        print("Contains:", p)
    else:
        print("No punctuation in this line of text.")
    if ',' in p:
        print("This line contains a comma")
    if l >= 0:
        print("Python is first used at {0}".format(1))
    print('-'*80)