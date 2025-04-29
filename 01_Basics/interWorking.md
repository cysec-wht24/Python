Say we have 2 variables with same value 10, now if we assign it to score then if we try toassign the same to a_score the python would rather than creating a new one would provide the same value's reference from the memory

say we have a id with value 5 (id = 5), now say the use of id is complete we don't need it anymore in memory, so now as there is no refeerence left for 5, you would think python's garbage collector would deallocate that 5 right ? BUT here there is a change in python internal working so how does python compiler optimizes this ?  

Python's compiler treats numbers and strings differently compared to list, dictionary and other datatypes as Python is a number powerful programming language

Now remember that value 10 was being referred by 2 variables score and a_score while 5 was being referenced by only one ie - id, so that means there must be a mechanismin in python, where counting of these references is being done 

You would be right then as wherever there is memory allocation there is a ref_count there with it, you won't be able to see it, if you try to see it the interpreter would do a lot of manipulation with you 

When you study compiler design, language design you will realize this is a very common thing thing being done by python, that in every language where memory references are done first then assignment of them  

So how can you see this reference count
you would first have import the sys library
import sys 
sys.getrefcount(24601)
it will give 3 why ?
sys.getrefcount('hitesh')
4294967295 why ? cause internally a compiler optimizer loop gets runned which almost everytime gives this number, this is not a problem its just that in python there is no easy way to reach memory so close that you get the reference count out of that 
sys.getrefcount(1)
4294967295
sys.getrefcount('h')
4294967295
Now you know ref_count exist but its just that you can't proof of existence everytime by printing it out but you can check it out in python documentation 

when we say a = 3, realize that 3's reference has been assigned to a

IMP: Datatype always remains in meory and  never goes to variable in python say score = 10, now here score has got nothing to do with if a value is string or integer or whatever, the datatype is given to the value in the memory if its a number or string, Thus python has no data type as you never assign datatype to an variable, but the reference inside the memory, or anything inside the memory has a datatype, and it's datatype is assigned inside memory only 

a = 3
a = 'chaiaurcode'
Now here you might think that 3's reference is no where so now python's garbage collector will come and collect 3 now that's is what happens majority of time but there is an exception 

Python's garbage collector does not immediately collect numbers and string, as lets take the above example python won't immediately collect 3 cause it knows that optimization is necessary and that 3's reference might come again from program somewhere, so just use the same 3 thus no need to redo assign and reassign again and again thus preventing computation power consumption. Thus numbers and string have late garbage collection, you can do it forcefully too


>>> a=5
>>> b=2
>>> a
5
>>> b
2
>>> a = a + 2
>>> a
7
>>>

In python before calculation, all reference values are retreived
Once that happens, the compute then goes to calculation, CPU or GPU, there are different ways and libraries that force you to do the calculation only on GPU or CPU
When the result 7 is came its reference is assigned to variable a but the value 5 is not immediately removed it's removed after sometime

