'''
Real World Example : Multiprocessing for CPU bound tasks
Scenerio : Factorial calculation
Factorial calculations, especially for large numbers
Involves signigicant computational work. Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance
'''

import multiprocessing
import math
import sys
import time

# increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# fucntion to compute factorial of a given number
def compute_factorial(number):
    print(f'Computing factorial of a {number}')
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result

if __name__ == "__main__":
    numbers = [5343, 7958, 3232, 5633, 5493]
    start = time.time()
    # create pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end = time.time()
    print(f'Results: {results}')
    print(f'Time taken for execution: {end - start}')
