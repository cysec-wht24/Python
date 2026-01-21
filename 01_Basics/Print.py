# ===============================
# 1. f-strings (Modern & Best)
# ===============================

name = "Manomay"
age = 22

print(f"My name is {name} and I am {age} years old")

# PROS:
# - Clean and very readable
# - Fastest method
# - Allows expressions inside {}
# CONS:
# - Python 3.6+ required


# ===============================
# 2. Comma-separated print
# ===============================

print("My name is", name, "and I am", age, "years old")

# PROS:
# - Simple and beginner-friendly
# - No string conversion needed
# CONS:
# - Less control over formatting
# - Adds spaces automatically


# ===============================
# 3. .format() method
# ===============================

print("My name is {} and I am {} years old".format(name, age))

# PROS:
# - Works in older Python versions
# - Flexible ordering
# CONS:
# - Verbose compared to f-strings
# - Harder to read for long strings


# ===============================
# 4. String concatenation (+)
# ===============================

print("My name is " + name + " and I am " + str(age) + " years old")

# PROS:
# - Very basic, easy to understand
# CONS:
# - Must convert non-strings manually
# - Error-prone and messy for large strings
# - Slower than f-strings
