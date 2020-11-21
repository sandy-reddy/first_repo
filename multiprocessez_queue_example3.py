from multiprocessing import Process, Value, Array, Lock
import os
import time
from multiprocessing import Pool


def cube(numbers):
    return numbers*numbers*numbers





if __name__ == "__main__":
    

    numbers = range (10)
    pool = Pool()

    result = pool.map (cube, numbers)

    pool.close()
    pool.join()

    print(result)


