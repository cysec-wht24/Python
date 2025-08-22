Say we have 2 variables with same value 10, now if we assign it to score then if we try to assign the same to a_score the python would rather than creating a new one would provide the same value's reference from the memory

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

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0] = 44
>>> l1
[44, 2, 3]
>>> p1 = [1, 2, 3]
>>> p2 = p1
>>> p2 = [1, 2, 3]
>>> p1[0] = 55
>>> p1
[55, 2, 3]
>>> p2
[1, 2, 3]
lists are mutable, changeable thus if they are changed new references are made 

>>> h1 = [1, 2, 3]
>>> h2 = h1[:]
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]

Now here we have done slicing thus we have made a copy cause if we would have said h2 = h1 that would be giving the same reference but because we have done slicing we have made a copy of it and provided it's reference 

>>> h1[0] = 55
>>> h1
[55, 2, 3]
>>> h2
[1, 2, 3]

Debate on Copy
>>> import copy
>>> h2 = copy.copy(h1)

there is something deeper copy which basically is calling listss from inside the list or nested list incase present 
>>> import copy
>>> h2 = copy.deepcopy(h1)

>>> n = [1, 2, 3]
>>> m = n
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m == n
True
>>> m is n
True
>>> n = [1, 2, 3]
>>> m == n
True
>>> m = [1, 2, 3]
>>> m == n
True
>>> m is n
False
>>>
All these concepts just to make you understand where you might be losing optimization in your code 
In python everywhere there is  dynamic reference type that in which variable there willbe array or string or else as these definations are kept inside memory






Chatgpt Refined notes from above 

# Python Memory and Variable Reference Notes

This is a friendly, self-study cheat sheet on how Python handles memory, variable references, and garbage collection. Think of it as a conversation with past-me: explanations, examples, and a pinch of humor.

## Variables and References

- In Python, **variables are just names referring to objects** in memory ([Variables in Python: Usage and Best Practices – Real Python](https://realpython.com/python-variables/#:~:text=In%20Python%2C%20variables%20are%20symbolic,variable_name)) ([Variables in Python: Usage and Best Practices – Real Python](https://realpython.com/python-variables/#:~:text=A%20Python%20variable%20is%20a,still%20contained%20within%20the%20object)). They don’t “contain” the data themselves; a variable points to the memory address where the actual object lives ([Variable and memory references in Python | by Rohit Patil | Medium](https://medium.com/@RohitPatil18/variable-and-memory-references-in-python-29f976772ad3#:~:text=At%20first%20glance%2C%20it%20might,where%20the%20actual%20data%20resides)) ([Variables in Python: Usage and Best Practices – Real Python](https://realpython.com/python-variables/#:~:text=In%20CPython%2C%20the%20standard%20Python,concrete%20objects%20stored%20in%20memory)). For example:

  ```python
  x = 100
  y = x
  ```

  Both `x` and `y` now refer to the *same* integer object `100`. We didn’t create a new number; we just made another reference (alias) to the existing `100` ([Variable and memory references in Python | by Rohit Patil | Medium](https://medium.com/@RohitPatil18/variable-and-memory-references-in-python-29f976772ad3#:~:text=At%20first%20glance%2C%20it%20might,where%20the%20actual%20data%20resides)) ([How to Copy a List in Python (5 Techniques w/ Examples)](https://www.dataquest.io/blog/python-copy-list/#:~:text=In%20fact%2C%20when%20you%20assign,a%20shared%20reference%20or%20object)). You can check with `id(x) == id(y)` to see they’re identical.

- If an object is mutable, multiple names pointing to it means changes via any name affect the object everywhere. For instance:

  ```python
  a = [1, 2, 3]
  b = a   # b references the same list as a
  b[0] = 'x'
  print(a)  # ['x', 2, 3], because a and b are the same list in memory.
  ```
  
  Assigning one variable to another doesn’t copy the object; it just creates a shared reference ([How to Copy a List in Python (5 Techniques w/ Examples)](https://www.dataquest.io/blog/python-copy-list/#:~:text=In%20fact%2C%20when%20you%20assign,a%20shared%20reference%20or%20object)) ([Variables in Python: Usage and Best Practices – Real Python](https://realpython.com/python-variables/#:~:text=Copied%21)). In other words, `a` and `b` both point to the same object.

- When you reassign a variable to a new value, Python makes it point to a different object. E.g.:

  ```python
  n = 300
  m = n  # both refer to 300
  m = 400  # now m points to 400, n still points to 300
  ```

  Now `m` and `n` refer to different integers. The old object (`300`) might become unreachable if no name points to it anymore. When an object’s reference count hits zero, Python will reclaim its memory ([Python Garbage Collection: Key Concepts and Mechanisms | DataCamp](https://www.datacamp.com/tutorial/python-garbage-collection#:~:text=Reference%20counting%20is%20the%20foundational,Here%20is%20how%20it%20works)) ([Variables in Python: Usage and Best Practices – Real Python](https://realpython.com/python-variables/#:~:text=When%20the%20references%20to%20an,is%20known%20as%20garbage%20collection)).

## Reference Counting and `sys.getrefcount()`

- CPython keeps a **reference count** for each object. Whenever a new reference to an object is created, the count goes up; when a reference is removed or goes out of scope, it goes down ([Python Garbage Collection: Key Concepts and Mechanisms | DataCamp](https://www.datacamp.com/tutorial/python-garbage-collection#:~:text=Reference%20counting%20is%20the%20foundational,Here%20is%20how%20it%20works)). When the count hits zero, the memory is freed immediately ([Variables in Python: Usage and Best Practices – Real Python](https://realpython.com/python-variables/#:~:text=When%20the%20references%20to%20an,is%20known%20as%20garbage%20collection)).
- You can inspect an object’s refcount with `sys.getrefcount(obj)`. Keep in mind `getrefcount` returns a number one higher than you might expect ([sys — System-specific parameters and functions — Python 3.13.3 documentation](https://docs.python.org/3/library/sys.html#:~:text=Return%20the%20reference%20count%20of,as%20an%20argument%20to%20getrefcount)) ([Fun with Python's sys.getrefcount()](http://groverlab.org/hnbfpr/2017-06-22-fun-with-sys-getrefcount.html#:~:text=In%20my%20experience%2C%203%20is,anywhere%20by%20default%20in%20Python)), because the act of passing the object to the function itself creates a temporary reference. For example:

  ```python
  import sys
  x = 10
  print(sys.getrefcount(x))  # e.g. 3: one for 'x', one internal, one for the function argument
  y = x
  print(sys.getrefcount(x))  # count increases by 1
  ```

  (Grover Lab noted that `sys.getrefcount(24601)` returned 3 as a baseline on his machine ([Fun with Python's sys.getrefcount()](http://groverlab.org/hnbfpr/2017-06-22-fun-with-sys-getrefcount.html#:~:text=In%20my%20experience%2C%203%20is,anywhere%20by%20default%20in%20Python)).) Also, some objects (like singletons or interned values) can have misleadingly high refcounts, so use this for *understanding*, not as an absolute measure ([sys — System-specific parameters and functions — Python 3.13.3 documentation](https://docs.python.org/3/library/sys.html#:~:text=Return%20the%20reference%20count%20of,as%20an%20argument%20to%20getrefcount)).
- **Circular references** are a special case: if two objects reference each other, their counts never drop to zero, even if nothing else references them. Ref-counting alone can’t clean these up, which is why Python also has a **generational garbage collector** to catch cycles ([Python Garbage Collection: Key Concepts and Mechanisms | DataCamp](https://www.datacamp.com/tutorial/python-garbage-collection#:~:text=Despite%20its%20efficiency%2C%20reference%20counting,generational%20garbage%20collection%20comes%20in)) (more on that below).

## Immutable Types: Ints and Strings (Interning)

- Immutable objects (like integers, strings, tuples) can’t be changed in place. When you “change” an immutable (e.g. `x = x + 1` for an int), Python actually creates a new object with the new value. For small immutables, CPython often reuses existing objects to save memory.
- For example, CPython **caches small integer objects** by default ([Integer Objects — Python 3.13.3 documentation](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong#:~:text=The%20current%20implementation%20keeps%20an,reference%20to%20the%20existing%20object)). All ints from -5 to 256 are pre-allocated. So:
  ```python
  a = 100
  b = 100
  print(a is b)  # True, since 100 is in the cached range.
  ```
  But:
  ```python
  x = 1000
  y = 1000
  print(x is y)  # Often False, because 1000 is not in the default cache.
  ```
  (There are subtleties—such as when literals appear in the same code block, CPython might intern them—but in general trust that *small ints* share one object ([Integer Objects — Python 3.13.3 documentation](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong#:~:text=The%20current%20implementation%20keeps%20an,reference%20to%20the%20existing%20object)) ([python - Is there a difference between "==" and "is"? - Stack Overflow](https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is#:~:text=In%20your%20case%2C%20the%20second,integers%2C%20this%20does%20not%20work)).)
- **Strings** are sometimes interned too. Identical string literals (especially short ones) may refer to the same object ([python - Does a slicing operation give me a deep or shallow copy? - Stack Overflow](https://stackoverflow.com/questions/19068707/does-a-slicing-operation-give-me-a-deep-or-shallow-copy#:~:text=In%20each%20case%2C%20the%20string,substantial%20memory%20and%20performance%20enhancement)) ([python - Is there a difference between "==" and "is"? - Stack Overflow](https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is#:~:text=The%20same%20holds%20true%20for,string%20literals)). For example:
  ```python
  s1 = "hello"
  s2 = "hello"
  print(s1 is s2)  # True, often they’re interned.
  s3 = "".join(["h", "ello"])
  print(s1 is s3)  # Likely False, since s3 was built at runtime.
  ```
  Ned Batchelder’s example shows that `'one'` ended up interned so all references were the same object ([python - Does a slicing operation give me a deep or shallow copy? - Stack Overflow](https://stackoverflow.com/questions/19068707/does-a-slicing-operation-give-me-a-deep-or-shallow-copy#:~:text=In%20each%20case%2C%20the%20string,substantial%20memory%20and%20performance%20enhancement)). Interning can make `is` tests look true for strings and small ints, but this is an implementation detail—you can’t rely on it. Always use `==` to check if values are equal.

## Mutable Types and Copying

- Lists, dictionaries, sets, and most user-defined objects are mutable. If you copy references, you end up with aliases (as we saw above). To make an actual copy of, say, a list, you have to do it explicitly.
- **Shallow copy with slicing or `list.copy()`:** This makes a new outer container but **references the same nested objects** ([python - Does a slicing operation give me a deep or shallow copy? - Stack Overflow](https://stackoverflow.com/questions/19068707/does-a-slicing-operation-give-me-a-deep-or-shallow-copy#:~:text=%40Davos%3A%20%60lst_copy,copies%20of%20the%20referenced%20objects)) ([Shallow vs Deep Copying of Python Objects – Real Python](https://realpython.com/python-copy/#:~:text=,to%20objects%20without%20copying%2C%20unlike)). For example:
  ```python
  original = [[1, 2], [3, 4]]
  shallow = original[:]  # or original.copy()
  shallow[0][0] = 'a'
  print(original)  # [['a', 2], [3, 4]]
  ```
  We changed a nested item and saw it in the original list, because the inner lists were shared ([python - Does a slicing operation give me a deep or shallow copy? - Stack Overflow](https://stackoverflow.com/questions/19068707/does-a-slicing-operation-give-me-a-deep-or-shallow-copy#:~:text=%40Davos%3A%20%60lst_copy,copies%20of%20the%20referenced%20objects)).
- **Deep copy:** To recursively clone everything (so the copy is fully independent), use `copy.deepcopy()`:
  ```python
  import copy
  original = [[1, 2], [3, 4]]
  deep = copy.deepcopy(original)
  deep[1][1] = 'b'
  print(original)  # [['a', 2], [3, 4]]  (original is unchanged)
  ```
  Deep copying makes new copies of all nested objects, so changes in the new structure won’t affect the original ([Shallow vs Deep Copying of Python Objects – Real Python](https://realpython.com/python-copy/#:~:text=,to%20objects%20without%20copying%2C%20unlike)).
- *Key point:* Simple assignment (`=`) just aliases. Slicing (`[:]`) or `list.copy()` gives a *shallow* copy. Use the `copy` module (`copy.copy` or `copy.deepcopy`) when you need deeper copies ([Shallow vs Deep Copying of Python Objects – Real Python](https://realpython.com/python-copy/#:~:text=,to%20objects%20without%20copying%2C%20unlike)) ([python - Does a slicing operation give me a deep or shallow copy? - Stack Overflow](https://stackoverflow.com/questions/19068707/does-a-slicing-operation-give-me-a-deep-or-shallow-copy#:~:text=%40Davos%3A%20%60lst_copy,copies%20of%20the%20referenced%20objects)).

## Equality (`==`) vs Identity (`is`)

- `==` checks if values are equal, whereas `is` checks if two names refer to the **exact same object** (same memory address) ([python - Is there a difference between "==" and "is"? - Stack Overflow](https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is#:~:text=,by%20the%20variables%20are%20equal)). For instance:
  ```python
  a = [1,2,3]
  b = [1,2,3]
  print(a == b)  # True (values equal)
  print(a is b)  # False (different objects in memory)
  ```
- Because of caching/interning, you might see `is` return True for small ints or short strings (e.g. `'a' is 'a'`). This can be confusing, but it’s an implementation detail ([python - Is there a difference between "==" and "is"? - Stack Overflow](https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is#:~:text=In%20your%20case%2C%20the%20second,integers%2C%20this%20does%20not%20work)) ([python - Is there a difference between "==" and "is"? - Stack Overflow](https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is#:~:text=The%20same%20holds%20true%20for,string%20literals)). The bottom line: **use `==` for equality checks**, and use `is` only when you explicitly want identity (for example, testing against `None`, since `None` is a singleton).  
- *Common tip:* Use `is` when checking `None` (e.g. `if x is None:`), but avoid using `is` for comparing other values ([python - Is there a difference between "==" and "is"? - Stack Overflow](https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is#:~:text=,by%20the%20variables%20are%20equal)).

## Garbage Collection (GC)

- In CPython, as soon as an object’s refcount goes to zero, its memory is reclaimed ([Python Garbage Collection: Key Concepts and Mechanisms | DataCamp](https://www.datacamp.com/tutorial/python-garbage-collection#:~:text=Reference%20counting%20is%20the%20foundational,Here%20is%20how%20it%20works)) ([Variables in Python: Usage and Best Practices – Real Python](https://realpython.com/python-variables/#:~:text=When%20the%20references%20to%20an,is%20known%20as%20garbage%20collection)). This means most objects are destroyed “immediately” when you lose all references (at least within that interpreter process).
- However, Python also uses a *generational garbage collector* for **cycles** ([Python Garbage Collection: Key Concepts and Mechanisms | DataCamp](https://www.datacamp.com/tutorial/python-garbage-collection#:~:text=Despite%20its%20efficiency%2C%20reference%20counting,generational%20garbage%20collection%20comes%20in)). If objects reference each other in a loop (A→B and B→A) and nothing else references them, their refcounts never drop to zero. The GC periodically runs to detect these unreachable cycles and free them. So destruction of cyclic garbage is *delayed* until the collector runs, not instantaneous.
- Another twist: if a class defines a `__del__` method (a destructor), it can complicate GC. In fact, one core Python developer warns that having `__del__` **guarantees delayed garbage collection**, because it makes cleanup more complex ([[Python-Dev] Adding a scarier warning to object.__del__?](https://groups.google.com/g/dev-python/c/iFlQm0j5lpU#:~:text=The%20reason%20we%20should%20warn,other%20methods%20are%20invoked%20from)). In practice, it’s best to avoid relying on `__del__` for critical cleanup (or use weak references) to avoid unexpected delays.
- You can manually trigger GC with `import gc; gc.collect()`, but usually Python handles it for you. In short, between refcount and the cyclic GC, Python will eventually clean up unreachable objects — you typically don’t have to micromanage every detail.

*End of notes. Remember: experiment with these concepts in a Python REPL (try `id()`, poke at `sys.getrefcount()`, play with list copies, etc.) to see how Python’s memory model actually behaves. Happy coding!* 

