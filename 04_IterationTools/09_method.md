>> Ds {'a': 1, 'b': 2}
>>> for key in D.keys():
...     print (key)
...
a
b
>>> I = iter()
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
>>>


the iter() object is inside files by default
>>> f = open('chai.py')
>>> 