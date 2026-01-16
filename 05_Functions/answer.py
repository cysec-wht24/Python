print("01.")
def square(number): 
    # number = parameter
    return number ** 2

result = square(2)
print(result)

print("----------------------------")
print("02.")

def add(numOne, numTwo):
    return numOne + numTwo


print(add(5, 5))

print("----------------------------")
print("03.")

def multiply(p1, p2):
    return p1 * p2


print(multiply(8, 5))
print(multiply('a', 5))
print(multiply(5, 'a'))

print("----------------------------")
print("04.")

import math

def circlecalci(r):
    return 2*math.pi*r, math.pi*(r**2)

print(circlecalci(7))

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(3)

print("Area: ", a, "Circumference: ", c)

print("----------------------------")
print("05.")
def greet(name = "User"):
    # if you provide a parameter then it becomes required
    return "Hello, " + name + " !"


print(greet("chai"))
print(greet())

print("----------------------------")
print("06.")
# Lambda function / Anonymous function -
# functions that have no name
# lambda is majorly used in frameworks like Django or flask
# along with in many libraries
cube = lambda x: x ** 3
print(cube(3))

print("----------------------------")
print("07.")
def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))

# *args: allows input of anynumber of parameters, 
# you need to add * to make it multiple param.
# use best practices only use arg rather than other
# words like chai, as you are handling arguments

# pass: a python keyword means "do nothing". 
# It's a placeholder used when a statement 
# is syntactically required, but you don’t 
# want any code to run.

print("----------------------------")
print("08.")
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="shaktiman", power="lazer")
# it does not matter if you define power first before name it still works
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")

print("----------------------------")
print("09.")
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

print("----------------------------")
print("10.")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(24))