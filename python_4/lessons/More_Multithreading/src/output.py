"""
output.py: The output thread for the miniature framework.
"""
identity = lambda x: x

import threading
class OutThread(threading.Thread):
    
    def __init__(self, N, q, sorting=True, *args, **kwargs):
        """Initialize thread and save queue references."""
        threading.Thread.__init__(self, *args, **kwargs)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []
    
    def run(self):
        """Extract items from the output queue and print until all done."""
        while self.workers:
            p = self.queue.get()
            if p is None:
                self.workers -= 1
            else:
                # This is a real output packet
                self.output.append(p)
        print("".join(c for (i, c) in (sorted if self.sorting else identity)(self.output)))
        print("Output thread terminiating")
