# Multiprocessing allows processes that run in parellel
# When to use multiprocessing
# 1 -> CPU Bound Task (Tasks that are heavy on CPU e.g., mathematical computation)
# 2 -> Parallel execution : While using multiple cores of cpu

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Square: {i * i}')

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Cube: {i * i * i}')

if __name__ == "__main__":
    # Create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    start = time.time()

    # start the process
    p1.start()
    p2.start()

    # Wait for the process to complete
    p1.join()
    p2.join()

    end = time.time()
    print(f'Time taken for execution: {end - start}')