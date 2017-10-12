# -----------
# Wed, 27 Sep
# -----------

"""
factorial()
iteration

reduce()
more iteration
"""

class A :
    def __init__ (self, v)
        self.v = v

x = A(2)    # x = A.__init__(2)
p = iter(x) # p = x.__iter__()

a = ???      # must be iterable
for v in a :
    ...

a = ???         # must be an iterable over iterables of size 2
for u, v in a :
    ...

"""
Questions
    What attribute makes something an iterable?
    	__iter__ 
    What attribute makes something an iterator?
    	__iter__ __next__
    What attribute makes something indexable?
    	__getitem__
    Why do containers not support next() directly?
    	because python created the __iter__ attribute so have the machinery to iterate
    	rather than creating the methods in the iterable classes
    When iterating over an iterable (not indexing) what must be true to be able to 
    modify the elements of the iterable?
    	we need to have a mutable iterable
    What's the relationship between a dict and the result of the keys(), values(), 
    and item() methods on the dict?
    	keys will give a list of all the keys of the dict
    	values will return a list of all the values in a dict
    	items will return a list of tuples that contain the key value pairs
"""
