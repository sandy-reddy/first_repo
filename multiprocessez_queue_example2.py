from multiprocessing import Process, Value, Array, Lock
import os
import time
from multiprocessing import Queue


numbers = range(1,6)


def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)


def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

                



if __name__ == "__main__":

    q = Queue()

    p1 = Process (target= square, args = (numbers, q))

    p2 = Process (target= make_negative, args = (numbers, q))


    p1.start()
    p1.join()

    p2.start()
    p2.join()
    

    
    nums = []

    while not q.empty():
        
        nums.append(q.get())
        
    print (nums)




