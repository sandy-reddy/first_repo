from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count() #using the same amount of processes as amount of cpus is a good benchmark

#creating processes

for i in range(num_processes):
    p = Process(target= square_numbers)
    processes.append(p)

#start each process
for p in processes:
    p.start()


#join
for p in processes:
    p.join()

#when running this file, open up activity monitor to see the multiple processes running concurently

