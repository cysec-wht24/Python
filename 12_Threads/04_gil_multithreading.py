# We use multiprocessing to actually avoid and bypass the GIL or Lock and actually speed up the process
# but cauting you are overriding the mutex value

from multiprocessing import Process
import time

def crunch_number():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...")

# multithreads not know the entry point like the threads
# thus need to add the below, referred to as the "dunder main" check, where "dunder" stands for "double underscore".
# __name__ is pronounced "dunder name"
# "__main__" is pronounced "dunder main"
# So this line is often informally called the "dunder name equals dunder main" pattern, or simply the "main guard".

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_number)
    p2= Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time with multi-processing is {end - start:.2f} seconds")