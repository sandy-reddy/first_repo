from threading import Thread, Lock, current_thread
import os
import time
from queue import Queue


def worker(q, Lock):
    while True:
        value = q.get()

        #processing
        with Lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()

if __name__ == "__main__":

    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range (num_threads):
        thread = Thread (target= worker, args=(q, lock))
        thread.daemon = True
        thread.start()


    for i in range(1, 21):
        q.put(i)

    q.join()

    print("end main")


