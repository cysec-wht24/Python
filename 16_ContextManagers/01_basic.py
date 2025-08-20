# docs = https://docs.python.org/3/reference/datamodel.html#context-managers

# A context manager is a Python construct that properly manages resources.
# It ensures resources (like files, network connections, database sessions, locks, etc.) are acquired and released correctly.
# The most common way you use it is with the with statement.

# Why use them:
# They guarantee cleanup (closing files, releasing resources).
# They avoid bugs like forgetting close().
# They make code cleaner and more Pythonic.

# Without context manager
f = open("file.txt", "w")
try:
    data = f.write()
finally:
    f.close()   # must close manually, or you risk memory leaks!

# With context manager 
with open("hello.txt", "w") as f:
    f.write("Hello World")
# File is auto-closed here, even if an error happens

# A context manager works because the object defines two special methods:
# __enter__ → runs when you enter the with block.
# __exit__ → runs when you leave the block (even if there’s an error).

# Python already has built- context managers
# open() (files)
# threading.Lock() (locks)
# decimal.localcontext() (decimal arithmetic settings)

# with → is just syntax, a “wrapper” that says:
# “Hey Python, enter this context, run my code, and when I’m done, clean up automatically.”
# Context managers → are objects that define how entering and exiting works (via __enter__ and __exit__ methods).
# with uses context managers

