"""
Program to test whether changing directory in one thread
changes the directory for a thread that already existed, or
a thread that is created after changing the directory.
"""
import os
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, sleeptime, change_dir, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.sleeptime = sleeptime
        self.change_dir = change_dir
    
    def run(self):
        print('{} has a path of {}'.format(self.name, os.getcwd()))
        if self.change_dir:
            os.chdir('V:\workspace\Python4_Homework10')
        print('{} finished after {} seconds with path {}'.format(self.name, self.sleeptime, os.getcwd()))

if __name__ == "__main__":
    t1 = MyThread(2, False)
    t1.start()
    t2 = MyThread(0, True)
    t2.start()
    t3 = MyThread(1, False)
    t3.start()