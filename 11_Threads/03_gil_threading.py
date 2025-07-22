# GIL = Global Interpreter Lock 
# The memory management is not thread safe. And to avoid the race 
# condition when two threads are trying to access or modify the same 
# object in the memory, then the race condition appears and Python 
# uses something known as gil, which provides a simple mutex so that 
# no two threads can actually change the memory at the same time.
# mutex is basiclly a locking system so only one can access at a time

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken: {end - start:.2f} seconds")