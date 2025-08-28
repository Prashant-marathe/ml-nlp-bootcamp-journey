# When to use multithreading ?
# 1 -> I/O bound tasks : Tasks that spent more time waiting for I/O operations (e.g., file operations, network requests)
# 2 -> Concurrent  Execution : When you want to improve the throughput of your application by performing multiple opeartions concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Number: {i}', sep=" ")

def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter: {letter}', sep=" ")

# Try using multiple threads so both functions can run concurrently and won't wait for other function to get executed completely.
#* Create multiple threads 
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

start = time.time()

#* start the thread :
t1.start()
t2.start()

# print_numbers()
# print_letters()

#* wait for the threads to complete
t1.join()
t2.join()

end = time.time()

print(f'Time taken for execution: {end - start}')

