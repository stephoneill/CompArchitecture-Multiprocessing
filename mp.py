import time
import math
import multiprocessing
from multiprocessing import Pool

# A function for timing a job that uses a pool of processes.
#  f is a function that takes a single argument
#  data is an array of arguments on which f will be mapped
#  pool_size is the number of processes in the pool. 
def pool_process(f, data, pool_size):
    tp1 = time.time()
    pool = Pool(processes=pool_size) # initialize the Pool.
    result = pool.map(f, data)       # map f to the data using the Pool of processes to do the work 
    pool.close() # No more processes
    pool.join()  # Wait for the pool processing to complete. 
    print("Results", result)
    print("Overall Time:", int(time.time()-tp1))
 

def my_func(x):
    s = math.sqrt(x)
    return s

# This verbose version shows which process in the pool is running each task. 
def my_func_verbose(x):
    s = math.sqrt(x)
    print("Task", multiprocessing.current_process(), x, s)
    return s

# Running in a Python environment
# import mp
# cw = range(10,15)
# mp.pool_process(mp.my_func_verbose, cw, 2)
