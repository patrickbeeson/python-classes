import unittest
import os
from memory_mapping import FileWriter


class TestMemoryMapping(unittest.TestCase):
    
    def setUp(self):
        self.fw1 = FileWriter('test', 1048576)
    
    def test_mm_file_size(self):
        self.fw1.make_mmap()
        f_size = os.path.getsize(os.path.join(os.getcwd(), 'test_mm.txt'))
        self.assertEqual(10485760, f_size)

    def test_write_file_size(self):
        self.fw1.make_write()
        f_size = os.path.getsize(os.path.join(os.getcwd(), 'test_w.txt'))
        self.assertEqual(10485760, f_size)


if __name__ == "__main__":
    unittest.main()
