Lets go back to iteration tools
we previously learned about functions for files - readline method, StopIteration exception and that file has its own iter() tool (this is default in python) eg - f = open(filename)
Now lets discuss about Lists and arrays, which don't have their own iter() tool
>>> myList = [1, 2, 3, 4] 
Question is there must be iteration tools that work on this as well, so does here also __next__ also comes in handy ?
>>> I = iter(myList)
>>> I
<list_iterator object at 0x102f4fa30>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x102f4fa30>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
StopIteration
>> |
The value inside I remains constant, basically meaning that if through the response if go to next element of iterable object with a start point memory address doesn't mean the this would change the memory address, this would be done internally done by the __next__ response, so the program basically says that it would keep point to the first, but internally there would be a pointer that would change from first address to the corresponding next address

So the memory reference does not change, memory reference se jo list iterator hota hai that would always point toward starting point
