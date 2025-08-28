# Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def print_numbers(numbers):
    time.sleep(1)
    return f'Number: {numbers}'

numbers = [1,2,2,3,2,3,3,2,3,5,56,7,5,6,7,8,6,6,6,7,7,765,5,5,5,6,8,5,5,4555,4,]

if __name__ == "__main__":
    start = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_numbers, numbers)
    end = time.time()

    for result in results:
        print(result)

    print(f'Time taken for execution: {end - start}')
