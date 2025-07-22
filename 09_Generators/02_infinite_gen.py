def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))

# Usecase:
# Simulating real-time sensor data
# Streaming log file lines for monitoring
# Generating an endless sequence of timestamps
# Creating infinite random test data
# Cycling through a set of tasks or resources (round-robin)
# Implementing game or animation loops
# Powering event-driven simulations
# Continuously reading from a socket or network feed
# Producing incremental IDs or tokens on demand
# Polling APIs at regular intervals
# Repeating scheduled tasks without using threads
# Serving data batches for machine learning training
# Endless music or image slideshow applications
# Driving a user interface loop until user exits