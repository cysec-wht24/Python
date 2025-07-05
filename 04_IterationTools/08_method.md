Now lets come back to the statement that files have by default their own iter() object
First we open the script 
>>> f = open('chai.py')
Now for list we had done this, we put myList inside iter and hold its reference
>>> I = iter(myList)
but we don't need to do this for file because for file the f has already by default behind the scene has done this -> iter(f)
so if you do something like this
>>> iter(f) is f
the output we would get is this 
True
Similarly, the following below
>>> iter(f) is f.__iter__()
True
Here f.__iter__() and f in the above code at same position is the same thing
>>> iter(f) is f this statement is only true for files in list it becomes false

Now we see the case for list just for comparison
>>> myNewList = [1, 2, 3]
for this list we were doing the below
>>> I = iter(myNewList)
But is this equal to this 
>>> iter(mynewList) is myNewList
we get the following output
False
>>>

So we get to prove from this that when we store the reference of a file inside a variable, then by default on its own its an iterable object, but if we have provided a reference of a list in a variable (aka a memory reference), then that varaible is not an iterable object of that list, its just the reference of that actual object