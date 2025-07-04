Python has made some iteration tool or loops
eg - for, comprehension, map

Iterable Objects - thing on which you are applying loop
eg - lists, file

Response
__next__

step 1) iteration tool does query on iterable objects, by sending an iter() Object/ method (aka internel pc) to iterable objects that says I need to apply an loop on you

step 2 ) We get two things in return generally one is a response that we can apply loop on iterable objects, we get a __next__ value as well with the response

step 3) Thus iterable Objects return a __next__, Iterable Object always point to the start location of the memory from where to start looping because from there we are getting complete memory allocation, never gives a full list

So how does the iteration tools knows that there are 4 values, how does it know the boundary, why does it not go out of the boundary ? How it knows that to start from first index for first value all these questions answer go inside the __next__ response header

So in the return from iterable Objects we get a 
(memory address that is at the start point) + (__next__)

__next__ = till we are getting __next__, at memory address the value is being printed, but it means another thing that more loops can be applied to potentially more values that exist in the memory address

say we have array [1, 2, 3, 4]
so the iteration tool recieves response like this - 
next()
next()
next()
than at final point 4 the final __next__ comes, then an exception is raised, stop iteration exception, this raising of exception signifies that there are no further values so we will not go forward

In python you can make any object iterable or non iterable depending if in internal property it has this __next__ response or not