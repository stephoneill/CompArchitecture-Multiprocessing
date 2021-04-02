import time
import math
import multiprocessing
from multiprocessing import Pool

def my_func(x):
    s = math.sqrt(x)
    return s

def my_func_verbose(x):
    s = math.sqrt(x)
    print("Task", multiprocessing.current_process(), x, s)
    return s

# A function for timing a job that uses a pool of processes.
#  f is a function that takes a single argument
#  data is an array of arguments on which f will be mapped
#  pool_size is the number of processes in the pool. 
def pool_process(f, data, pool_size):
    if __name__ == '__main__':
        with multiprocessing.get_context('fork').Pool(processes=pool_size) as pool:
            tp1 = time.time()
            print(data, pool_size)
            # pool = Pool(processes=pool_size) # initialize the Pool.
            result = pool.map(f, data)       # map f to the data using the Pool of processes to do the work 
            pool.close() # No more processes
            pool.join()  # Wait for the pool processing to complete. 
            print("Results", result)
            print("Overall Time:", int(time.time()-tp1))


def check_prime(num):
    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                print("Time:", int(time.time()-t1))
                break
        else:
            print(num,"is a prime number")
            print("Time:", time.time()-t1) 
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    return res

# dataRange = range(10)

# Use the pool_process function to apply my_func to the data in dataRange.  
# This task is so light it requires very little processing time. 
# pool_process(my_func_verbose, dataRange, 2)

dataRange = [61, 67, 71, 73, 79, 83, 89, 97, 101, 15488801] # list of known prime numbers

pool_process(check_prime, dataRange, 2)