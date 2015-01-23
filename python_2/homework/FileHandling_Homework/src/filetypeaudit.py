import os
from collections import Counter as counter
from operator import itemgetter
import glob

def filetypeaudit():
    """ Function to return file types with counts in
    current working directory. Will also print this
    information. """
    # Get our current working directory
    cwd = os.getcwd()
    # Get a list of directory contents
    f_lst = glob.glob('*')
    # Create a list for file types
    ext_lst = []
    for ft in f_lst:
        # No directories, only files
        if os.path.isfile(ft):
            ft = os.path.splitext(ft)[1]
            if ft == '':
                ft = 'unknown type'
            ext_lst.append(ft)

    # Build a dict of extensions with counts
    ext_ct_lst = counter(ext_lst)
    # Sort our list from small to large
    sorted_lst = sorted(ext_ct_lst.items(), key=itemgetter(0))
    # Print our list of extensions and counts
    print('Directory contents:')
    for item in sorted_lst:
        print('{}: {}'.format(item[0] ,item[1]))
    # Return our dict of extensions and counts
    return ext_ct_lst
        
if __name__ == "__main__":
    filetypeaudit()