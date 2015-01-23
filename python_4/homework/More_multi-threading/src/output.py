"""
output.py: The output thread for the miniature framework.
"""
identity = lambda x: x

import threading
import time

class OutThread(threading.Thread):
    
    def __init__(self, N, q, start_time, sorting=True, *args, **kwargs):
        """Initialize thread and save queue references."""
        threading.Thread.__init__(self, *args, **kwargs)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []
        self.start_time = start_time
    
    def run(self):
        """Extract items from the output queue and print until all done."""
        while self.workers:
            p = self.queue.get()
            if p is None:
                self.workers -= 1
            else:
                # This is a real output packet
                self.output.append(p)
        # Timing
        total_time = time.time() - self.start_time
        # print the length of the output
        print(len(self.output))
        print("Output thread terminiating. Total run time: {}".format(total_time))
