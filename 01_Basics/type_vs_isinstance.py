# type()
# Used to get the exact type of an object.
x = 10
type(x) == int   # True

# type() does not support inheritance.
# Checks only the exact class, not parent classes.
class Animal:
    pass

class Dog(Animal): 
    pass

d = Dog()
type(d) == Dog # True
type(d) == Animal   # False

# for that usecase isinstance() is preffered
# Checks whether an object is an instance of a class or its parent class.
isinstance(10, int)        # True
isinstance("hi", str)      # True

# Supports inheritance:
isinstance(d, Animal)      # True

# Supports multiple types:
isinstance(x, (int, float))

# | Feature           | type() | isinstance() |
# | ----------------- | ------ | ------------ |
# | Inheritance aware | ❌      | ✅            |
# | Multiple types    | ❌      | ✅            |
# | Recommended       | ❌      | ✅            |

# Use isinstance() when checking types in real code, especially with:
# -> OOP
# -> Input validation
# -> Polymorphism