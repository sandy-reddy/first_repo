from threading import Thread, Lock
import os
import time
from queue import Queue

if __name__ == "__main__":

    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)

    first = q.get()
    print(first)

    q.task_done() #tells that the task is done after u call q.get()
    q.join() # blocks until all items in queue have been proccessed. Similar to the thread.join()


    print("end main")


