# Multithreading with thread pool executer

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(numbers):
    time.sleep(1)
    return f'Number: {numbers}'
numbers = [1,2,3,4,4,2,3,5,45,6,4,7,4,3,4,6,4,4,33,3,7,6,33,5,5,4,33]

start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)
end = time.time()

for result in results:
    print(result)

print(f'Time taken for execution: {end - start}')