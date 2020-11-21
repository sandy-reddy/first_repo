from threading import Thread
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

threads = []
num_threads = 10 #using the same amount of processes as amount of cpus is a good benchmark

#creating processes

for t in range(num_threads):
    t = Thread(target= square_numbers)
    threads.append(t)

#start each process
for t in threads:
    t.start()


#join : will wait for them to complete 
for t in threads:
    t.join()



#when running this file, open up activity monitor to see the multiple threads running concurently

