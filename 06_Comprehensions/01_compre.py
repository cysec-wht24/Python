# comprehensions are a concise way to create lists, sets, dictionaries or generators
# in python using a single line of code
# They are used in filtering items, transforming items like INR -> USD, create a new collection
# or if you want to  flatten nested structures
# Purpose they serve => cleaner code and faster execution
# Types of Comprehensions:
# List, Set, Dictionary, Generator
# Format: [expression for item in iterable if condition]
# Check docx:
# https://docs.python.org/3.15/tutorial/datastructures.html#list-comprehensions

menu = {
    "Masala",
    "iced",
    "Peach",
    "Ginger"
}

iced_tea = [tea for tea in menu if "iced" in tea]
print(iced_tea)