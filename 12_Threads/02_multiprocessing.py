# Concurrency: Multiple tasks in progress at the same time (but not necessarily simultaneously).
# Parallelism: Multiple tasks executing at the same time (literally at the same instant).
# Multithreading: Running multiple threads in the same process (can be concurrent, but not parallel in CPython).
# Context Switching: Switching between tasks by saving and restoring their state. Common in concurrency.

from multiprocessing import Process
import time

# parallelism is only possible using multiprocessing
def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
        for i in range(3)
    ]

    # Start all process
    for p in chai_makers:
        p.start()

    # wait for all to complete
    for p in chai_makers:
        p.join()

    print("All chai served")

# "Parallelism = multithreading" => ❌ In Python, multithreading is concurrent, not parallel (due to the GIL)
# "Concurrency = context switching" => ✅ Mostly true for threading; also true in async via task switching
# "Parallelism = multiprocessing" => ✅ Correct. True parallelism in Python is achieved through multiprocessing