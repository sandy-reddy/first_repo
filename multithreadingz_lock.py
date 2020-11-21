from threading import Thread, Lock
import os
import time

data_base_value = 0


def increase(lock):
    global data_base_value

    lock.acquire()       #lock
    local_copy = data_base_value
    local_copy += 1
    time.sleep(0.1)
    data_base_value = local_copy
    lock.release()          #lock

if __name__ == "__main__":
    
    
    lock = Lock()     #creating lock object
    print ("start value", data_base_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("end value", data_base_value)

    print("end main")
    