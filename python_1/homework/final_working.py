#!/usr/local/bin/python3

from string import punctuation

class ComputeText:
   
    def __init__(self, filename):
       self.filename = filename

    def compute_length(self):
        file = ComputeText(self.filename)
        with open(file, 'r') as f: 
            data = f.read()

            for punc in punctuation:
                text = f.replace(punc, "")
    
            word_list = text.split()
    
            for i, word in enumerate(word_list, 1):
                i = word_position
                word_length = len(word)
            return word_position, word_length

    def compute_words(word_position, word_length):
        """ This program reads input from a file, 
        splits the words, and computes the length of each word.
        It then prints a table showing the word count for each
        of the word lengths.

        >>> compute_words('filename_test.txt')
        Length Count
        1 4
        2 2
        3 1
        4 4
        """
        return "Length Count\n{} {}".format(word_position, word_length)

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    #_test()
    result = ComputeText.filename('declaration.txt')
    print(result)