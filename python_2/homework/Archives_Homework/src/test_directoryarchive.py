import unittest
import os
import shutil
import zipfile
import directoryarchive

class TestDirectoryArchive(unittest.TestCase):
    
    def setUp(self):
        self.path = r"v:\workspace\archive_test"
        self.zip_filename = os.path.join(self.path, "archive.zip")
        os.mkdir(self.path)
        self.file_names = ['road', 'cyclocross', 'track', 'mountain']
        for fn in self.file_names:
            f = open(os.path.join(self.path, fn), 'w')
            f.close()
   
    def test_function_can_zip_path_specified(self):
        directoryarchive.zip_dir(self.path)
        zf = zipfile.ZipFile(self.zip_filename, "r")
        files_in_archive = zf.namelist()
        zf.close()
        print(files_in_archive)
        expected = set(['archive_test/'+fn for fn in self.file_names])
        observed = set(files_in_archive)
        self.assertEqual(observed, expected)
        
    def tearDown(self):
        os.remove(self.zip_filename)
        shutil.rmtree(self.path, ignore_errors=True)

if __name__ == "__main__":
    unittest.main()
