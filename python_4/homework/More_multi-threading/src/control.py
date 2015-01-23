"""
control.py: Creates queues, starts ouput and worker threads, and pushes inputs into the input queue.
"""
from queue import Queue
from output import OutThread
from worker import WorkerThread
from random import choice
from string import ascii_lowercase
import time

START_TIME = time.time()

WORKERS = 10

inq = Queue(maxsize=int(WORKERS*1.5))
outq = Queue(maxsize=int(WORKERS*1.5))

ot = OutThread(WORKERS, outq, START_TIME)
ot.start()

for i in range(WORKERS):
    w = WorkerThread(inq, outq)
    w.start()
# Generate a random string of 1000 alphabetic characters
instring = ''.join([choice(ascii_lowercase) for i in range(1000)])
for work in enumerate(instring):
    inq.put(work)
for i in range(WORKERS):
    inq.put(None)
inq.join()
print("Control thread terminating")
