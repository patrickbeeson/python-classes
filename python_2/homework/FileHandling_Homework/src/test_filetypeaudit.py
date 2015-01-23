import unittest
import os
from filetypeaudit import filetypeaudit
import tempfile
import shutil

class TestFileTypeAudit(unittest.TestCase):
    """ Test case to verify reading of files
    and output of their file types from working
    directory. """
    
    def setUp(self):
        """ Set up our test and fixtures """
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp('tempdir')
        os.chdir(self.dirname)
        os.mkdir('testdir')
        self.file_names = ["file.txt", "file2.txt", "file.doc", "file.py", "noext"]
        for fn in self.file_names:
            f = open(fn, "w")
            f.close()
            
    def test_print_file_type_audit(self):
        """
        Test whether our function returns the file types and counts of each type.
        """
        expected = {'.txt': 2, '.doc': 1, '.py': 1, 'unknown type': 1}
        self.assertEqual(
            expected,
            filetypeaudit(),
            """
            The directory contains 1 directory, 2 .txt files, 1 .doc file,
             1.py file, and one file with no extension.
            """
        )

    def teardown(self):
        """ Delete our fixtures """
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()
    
    