>>> for line in open('chai.py):
...    print(line)
...
import time

print("chai is here")

username = "hitesh"

print(username)
>>> 

Now question for you - How did it know that the loop needs to end the moment it recieves empty string ?
Because these are iteratable tools, inside these tools iterable programming is already done on how to read a file ?
how when empty string '' comes then we need to stop and more
Now there a one line gap between each because the /n is not properly read thus you can do this as well 

>>> for Line in open('chai.py'):
print(line, end='')

import time
print("chai is here")
username = "hitesh"
print(username)>>>