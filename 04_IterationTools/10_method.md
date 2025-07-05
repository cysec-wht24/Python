Range is iterable as well
>>> range(5)
range(0, 5)
>>> R = range[&)
>>> R
range(0, 5)
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next (I)
4
>>> next (I)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
>>> |