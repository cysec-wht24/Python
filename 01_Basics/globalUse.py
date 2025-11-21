# Global is not needed for modifying mutable objects (lists, dicts, set) passed into a function; only needed if you reassign the variable itself.
# Note: variable inside aa function are local by default, global tells python to use global variable instead of creating local one 
# Useful for: counters, configuration flags, or caching data across functions

x = 10

def update_x():
    x = 20        # this creates new local variable x, global x remains unchanged

update_x()
print(x)          # Output: 10

y = 10  # global variable

def update_y():
    global y      # refers to global y
    y = 20        # modifies global y

update_y()
print(y)          # Output: 20


arr = [1,2,3,5]

# modifying
def update_arr(num):
    arr.append(num)

update_arr(7)    
print(arr)

def reassign_arr():
    arr = [5]

reassign_arr()
print(arr) # Output does not change

def actually_arr():
    global arr
    arr = [21]

actually_arr()
print(arr)