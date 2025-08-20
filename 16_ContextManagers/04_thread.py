import threading

lock = threading.Lock()
with lock:
    print("Lock acquired safely!")
    # do critical section work
# lock is released here automatically

# without with
# lock.acquire()
# try:
#     print("Lock acquired safely!")
# finally:
#     lock.release()
