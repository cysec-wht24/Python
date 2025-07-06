def greet(name = "User"):
    # if you provide a parameter then it becomes required
    return "Hello, " + name + " !"


print(greet("chai"))
print(greet())