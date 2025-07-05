__next__ is core syntax that makes object iterable. This is the raw way of reading files in python thus exceptions are not handled well here

>>> f = open('chai.py')
>>> f.__next__()
‘import time\n'
>>> f.__next__()
'print ("chai is here")\n'
>>> f.__next__()
‘username = "hitesh"\n'
>>> f.__next__()
‘print (username)'
>>> f.__next__()
Traceback (most recent call last):
File "<stdin>", Line 1, in <module>
StopIteration
>>>
