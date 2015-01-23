"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp('testdir')
        os.chdir(self.dirname)
        
    def test_1(self):
        """
        Verify files are created, and match
        what's expected in our temp directory.
        """
        file_list = ['this.txt', 'that.txt', 'the_other.txt']
        for filename in file_list:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        self.assertEqual(set(file_list), set(os.listdir(self.dirname)))
    
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        "Verify binary file size"
        with open('binaryfile.bin', 'wb') as fb:
            fb.write(bytes('\0', 'UTF-8') * 1000000)
        self.assertEqual(os.stat('binaryfile.bin').st_size, 1000000)
            
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()
