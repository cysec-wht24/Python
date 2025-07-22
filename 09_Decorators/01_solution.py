# decorators: 

import time
# no usecase with the decorator
# decorator is basically where we make a 
# method inside which we make another method 
# inside which we pass any function to execute 
# it and return the wrapper. Look at a decorator as a toll booth 
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_funtion(n):
    time.sleep(n)

example_funtion(2)