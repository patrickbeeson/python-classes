"""
memory_mapping.py: Program to test timing for two methods of creating a 10mb file.
The first uses a memory-mapped file, while the second uses the write() method.
"""
import mmap
import os
import time
import random
from timeit import Timer

# 10 MB
FILE_SIZE = 10485760

class FileWriter(object):
    """
    A file writer object.
    """
    def __init__(self, filename, chunksize):
        self.filename = filename
        self.chunksize = chunksize
        self.dir = os.getcwd()
    
    def make_mmap(self):
        fn = self.filename + '_mm.txt'
        n = int(FILE_SIZE / self.chunksize)
        with open(os.path.join(self.dir, fn), 'w+b') as f:
            mm = mmap.mmap(f.fileno(), FILE_SIZE)
            for i in range(n):
                chunk = bytearray(random.getrandbits(8) for i in range(self.chunksize))
                offset = i * self.chunksize
                mm[offset:offset + self.chunksize] = chunk
            mm.flush()
            mm.close()

    def make_write(self):
        fn = self.filename + '_w.txt'
        n = int(FILE_SIZE / self.chunksize)
        with open(os.path.join(self.dir, fn), 'wb') as f:
            for i in range(n):
                chunk = bytearray(random.getrandbits(8) for i in range(self.chunksize))
                f.write(chunk)

if __name__ == "__main__":
    # Timer tests for each method on FileWriter using progressively smaller chunks
    mm_lrg_mb_chunk = Timer("FileWriter('test1', 1048576).make_mmap()", "from __main__ import FileWriter")
    mm_med_mb_chunk = Timer("FileWriter('test2', 524288).make_mmap()", "from __main__ import FileWriter")
    mm_sml_mb_chunk = Timer("FileWriter('test3', 262144).make_mmap()", "from __main__ import FileWriter")
    print("mmap using one mb chunk: ", mm_lrg_mb_chunk.timeit(number=1))
    print("mmap using half mb chunk: ", mm_med_mb_chunk.timeit(number=1))
    print("mmap using quarter mb chunk: ", mm_sml_mb_chunk.timeit(number=1))

    w_lrg_mb_chunk = Timer("FileWriter('test1', 1048576).make_write()", "from __main__ import FileWriter")
    w_med_mb_chunk = Timer("FileWriter('test2', 524288).make_write()", "from __main__ import FileWriter")
    w_sml_mb_chunk = Timer("FileWriter('test3', 262144).make_write()", "from __main__ import FileWriter")
    print("write using one mb chunk: ", w_lrg_mb_chunk.timeit(number=1))
    print("write using half mb chunk: ", w_med_mb_chunk.timeit(number=1))
    print("write using quarter mb chunk: ", w_sml_mb_chunk.timeit(number=1))

