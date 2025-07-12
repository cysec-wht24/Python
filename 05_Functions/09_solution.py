# yield: keyword is used in a function to turn 
# it into a generator. A generator is a 
# special kind of iterator that allows you 
# to pause the function’s execution and resume 
# it later, remembering its state.

# In python nothing is inclusive of last parameter

# def even_generator(limit):
#     li = []
#     for i in range(2, limit + 1, 2):
#         li.append(i)
#     return li
# This would give us a list wwhich we don't want, 
# we want one number at a time 

# we could also apply a loop outsidde the function 
# but remember int type is not iterable so this will throw error
# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         return i

# for num in even_generator(10):
#     print(num)
# We need to yield the value and remember it in memory as well
# so that we can move to net value and not be stuck at same position
# python will manage internally on its owwn to keep its reference 
# in separate memory for each loop calling.

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num) 