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
