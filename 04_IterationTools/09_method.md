Dictionaries are also iterable
>>> D = {'a': 1, 'b': 2}
>>> for key in D.keys():
...     print(key)
...
a
b
Now if we want to do it manually 
Now if we give D inside iter() and if it is actually iterable then I would successfully get its reference
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x102f81990>
>>> next (I)
'a'
>>> next (I)
'b'
>>> next(I)
Traceback (most recent call last):
 File "<stdin>", Line 1, in <module>
StopIteration
=> exception raised
>>>