# Mutable: Value can be changed in place after creation of object
# Immutable: Value can't be changed, instead Python creates new object on change

# Why Matters ? (! USECASE BASED !)
# Performance: modifying a mutable object is faster than creating new objects repeatedly.
# Memory Usage: Mutable objects reuse memory. Immutable objects create new memory each time.
# Function Argument Behavior: Mutables can be changed inside functions, immutables cannot.
# Hashability: Immutable types can be used as: dictionary keys, set elements. Mutable types cannot.

# -------------------------
# MUTABLE DATA TYPES
# -------------------------

# LIST
a = [1, 2, 3]
print("List before:", a)
a.append(4)
print("List after:", a)

# SET
s = {1, 2}
print("\nSet before:", s)
s.add(3)
print("Set after:", s)

# DICTIONARY
d = {"x": 1, "y": 2}
print("\nDict before:", d)
d["x"] = 999
print("Dict after:", d)

# BYTEARRAY
b = bytearray(b"hello")
print("\nBytearray before:", b)
b[0] = 72
print("Bytearray after:", b)

# ARRAY
import array
arr = array.array('i', [1, 2, 3])
print("\nArray before:", arr)
arr[0] = 9
print("Array after:", arr)


# -------------------------
# IMMUTABLE DATA TYPES
# -------------------------

# INT
x = 10
print("\nInt IDs:", id(x), end=" → ")
x = x + 1
print(id(x))

# FLOAT
x = 10.22
print("Float IDs:", id(x), end=" → ")
x = x + 1.44
print(id(x))

# BOOLEAN
flag = True
print("\nBool IDs:", id(flag), end=" → ")
flag = False
print(id(flag))

# STRING
s = "hello"
print("String ID before:", id(s))
s = s + " world"
print("String ID after:", id(s))

# TUPLE
t = (1, 2, 3)
print("\nTuple:", t)

# FROZEN SET
fs = frozenset([1, 2, 3])
print("Frozen set:", fs)

# BYTES
b = b"hello"
print("Bytes:", b)