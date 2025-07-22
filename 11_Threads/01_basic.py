# Concurrency: 
#   threading.Thread 
#   asyncio

# Parallelism:
#   multiprocessing.Process 
#   concurrent.futures.ProcessPoolExecutor


# This is Concurrency - we have one single code doing the task but we were able to get multiple things done
import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(1) # assuming operation takes time

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(2)

# create threads by default does nothing
# concurrrency = context switching
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

# now invoke or start the initialized thread
# multithreading example
order_thread.start()
brew_thread.start()

# wait for both to finish => wait until the thread terminates
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")