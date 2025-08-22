# global is not needed for modifying mutable objects (lists/dicts) 
# passed into a function; only needed if you reassign the variable itself.
# Note: variable inside aa function are local by default, global tells python
# to use global variable instead of creating local one 
# Useful for: counters, configuration flags, or caching data across functions

x = 10

def update_x():
    x = 20        # local variable, global x remains unchanged

update_x()
print(x)          # Output: 10

y = 10  # global variable

def update_y():
    global y      # refers to global x
    y = 20        # modifies global x

update_y()
print(y)          # Output: 20